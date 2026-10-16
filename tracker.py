$text = Get-Clipboard -Raw
[System.IO.File]::WriteAllText("$PWD\tracker.py", $text, [System.Text.UTF8Encoding]::new($false))