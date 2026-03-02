#!/usr/bin/env python3
"""
Import .eml files from eml_drafts/ into Microsoft Outlook for Mac as draft emails.

Usage: python3 create_outlook_drafts.py
"""

import email
import glob
import html as html_mod
import os
import re
import subprocess
import sys
import tempfile
import time


def plain_text_to_html(text):
    """Convert plain text to HTML with clickable links."""
    url_pattern = re.compile(r'(https?://[^\s)<>]+)')
    result = []
    last_end = 0
    for match in url_pattern.finditer(text):
        # Escape the text before this URL
        result.append(html_mod.escape(text[last_end:match.start()]))
        # Add the URL as a clickable link (escape display text, keep href raw)
        url = match.group(1)
        result.append(f'<a href="{url}">{html_mod.escape(url)}</a>')
        last_end = match.end()
    # Escape any remaining text after the last URL
    result.append(html_mod.escape(text[last_end:]))
    html_str = "".join(result).replace("\n", "<br>")
    return (
        '<html><body style="font-family: Calibri, sans-serif; font-size: 11pt;">'
        + html_str
        + "</body></html>"
    )


def create_outlook_draft(to_addr, subject, body, from_addr=None):
    """Create a draft email in Outlook via AppleScript."""
    html_body = plain_text_to_html(body)
    with tempfile.NamedTemporaryFile(
        mode="w", suffix=".html", delete=False, encoding="utf-8"
    ) as tmp:
        tmp.write(html_body)
        tmp_path = tmp.name

    try:
        escaped_subject = subject.replace("\\", "\\\\").replace('"', '\\"')
        escaped_to = to_addr.replace("\\", "\\\\").replace('"', '\\"')

        applescript = f'''
        set bodyText to read POSIX file "{tmp_path}" as «class utf8»
        tell application "Microsoft Outlook"
            set newMsg to make new outgoing message with properties {{subject:"{escaped_subject}", content:bodyText}}
            make new to recipient at newMsg with properties {{email address:{{address:"{escaped_to}"}}}}
            open newMsg
            delay 1
            close window 1 saving yes
        end tell
        '''

        result = subprocess.run(
            ["osascript", "-e", applescript],
            capture_output=True, text=True
        )
        if result.returncode != 0:
            raise RuntimeError(f"AppleScript error: {result.stderr.strip()}")
    finally:
        os.unlink(tmp_path)


def parse_eml(filepath):
    """Parse an .eml file and return (to, subject, body)."""
    with open(filepath, "rb") as f:
        msg = email.message_from_binary_file(f)

    to_addr = msg["To"]
    subject = msg["Subject"] or ""
    from_addr = msg["From"] or ""

    # Decode body
    if msg.is_multipart():
        for part in msg.walk():
            if part.get_content_type() == "text/plain":
                body = part.get_payload(decode=True).decode(
                    part.get_content_charset() or "utf-8"
                )
                break
        else:
            body = ""
    else:
        body = msg.get_payload(decode=True).decode(
            msg.get_content_charset() or "utf-8"
        )

    return to_addr, subject, body, from_addr


def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    eml_dir = os.path.join(script_dir, "eml_drafts")

    eml_files = sorted(glob.glob(os.path.join(eml_dir, "*.eml")))
    if not eml_files:
        print("No .eml files found in eml_drafts/")
        sys.exit(1)

    print(f"Found {len(eml_files)} .eml files")

    batch_size = 10
    success = 0
    errors = []

    for i, filepath in enumerate(eml_files):
        filename = os.path.basename(filepath)
        try:
            to_addr, subject, body, from_addr = parse_eml(filepath)
            create_outlook_draft(to_addr, subject, body, from_addr)
            success += 1
            print(f"  [{success}/{len(eml_files)}] {filename} -> {to_addr}")
        except Exception as e:
            errors.append((filename, str(e)))
            print(f"  [ERROR] {filename}: {e}")

        # Pause between batches to avoid overwhelming Outlook
        if (i + 1) % batch_size == 0 and (i + 1) < len(eml_files):
            print(f"  -- Pausing 60s after batch of {batch_size} --")
            time.sleep(60)

    print(f"\nDone! Created {success} drafts in Outlook.")
    if errors:
        print(f"{len(errors)} errors:")
        for name, err in errors:
            print(f"  - {name}: {err}")


if __name__ == "__main__":
    main()
