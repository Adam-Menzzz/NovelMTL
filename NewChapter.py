def create_html_with_chapter(chapter_number, chapter_content, html_filename):
  try:
    html_content = f'''<!DOCTYPE html>
<html lang="en-US">
<head>
<title>Zenith Zombie MTL</title>
<link rel='stylesheet' href="styles.css">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<link rel="icon" type="image/x-icon" href="../pic.png">
</head>
<body>
  <div id="navbar-placeholder"></div>
  <div class="chapter-container">
    <h1>Chapter {chapter_number}</h1>
    <div class ="chapter" id="chapter">{chapter_content}</div>
    <div class="navigation">
      <button class="nav-button" onclick="prevChapter()">Previous Chapter</button>
      <button class="nav-button" onclick="nextChapter()">Next Chapter</button>
    </div>
  </div>
  <script type="text/javascript" src="../navbar.js"></script>
  <script type="text/javascript" src="../spacing.js"></script>
  <script>
    function nextChapter() {{
        window.location.href = `VWPWE-{chapter_number+1}.html`;
    }}
    function prevChapter() {{
        window.location.href = `VWPWE-{chapter_number-1}.html`;
    }}
  </script>
</body>
</html>'''

    with open(html_filename, 'w') as html_file:
      html_file.write(html_content)

    print(f'HTML file "{html_filename}" has been successfully created.')
  except Exception as e:
    print(f'An error occurred: {e}')

if __name__ == "__main__":
  chapter_number = 1000
  chapter_content = ''''''
  html_filename = f"VirtualWorldPeerlessWhiteEmperor/VWPWE-{chapter_number}.html"
  create_html_with_chapter(chapter_number, chapter_content, html_filename)