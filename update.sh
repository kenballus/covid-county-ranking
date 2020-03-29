while  [ true ]; do
    python3 scrape.py
    git add .
    git commit -m "Update data"
    git push
    sleep 900 # 15 minutes
done
