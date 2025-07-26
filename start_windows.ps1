# Start Django server in new window
Start-Process -NoNewWindow -FilePath "python" -ArgumentList "manage.py runserver 0.0.0.0:8100" -WorkingDirectory $PWD

# Start frontend server in new window
Start-Process -NoNewWindow -FilePath "bun" -ArgumentList "run dev --port 5173" -WorkingDirectory (Join-Path $PWD "frontend")
