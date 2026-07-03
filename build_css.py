css = '''    <style>
        :root {
            --bg-deep: #08090D;
            --bg-card: #0D0F14;
            --bg-surface: #11141A;
            --bg-elevated: #161A23;
            --border: #1C1F26;
            --border-light: #2A2F3A;
            --text-primary: #EAECEF;
            --text-secondary: #9CA3AF;
            --text-muted: #6B7280;
            --accent: #00D4FF;
            --primary: #00E676;
            --critical: #EF4444;
            --high: #F59E0B;
            --medium: #10B981;
            --low: #3B82F6;
            --font-mono: 'JetBrains Mono', monospace;
            --font-sans: 'Inter', sans-serif;
        }
'''
with open('index.html', 'a', encoding='utf-8') as f:
    f.write(css)
print('CSS variables OK')
