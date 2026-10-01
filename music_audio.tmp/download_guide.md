# 🎬 YouTube 音乐下载操作指南

本文档记录从 YouTube 下载背景音乐并转换为 WAV 格式的标准流程，供后续参考。

---

## 一、环境要求

```bash
# macOS
brew install yt-dlp ffmpeg
```

| 工具 | 用途 |
|---|---|
| `yt-dlp` | YouTube 视频/音频下载 |
| `ffmpeg` | 音频格式转换（WebM/Opus → WAV） |

---

## 二、目录结构约定

```
music_audio/
├── download_guide.md          ← 本文档
├── curated_tracks.md          ← 各博主精选曲目汇总
├── .gitignore                 ← 排除 *.wav / *.mp3 / *.flac
├── {creator-name}/            ← 按博主/来源分目录
│   ├── music.md               ← 该来源的完整播放列表文档
│   ├── playlist_entries.jsonl ← yt-dlp 导出的元数据（可选）
│   └── NN-videoID-Title.wav   ← 下载的音频文件
```

**命名规范**：`{序号}-{videoID}-{标题}.wav`

---

## 三、下载命令

### 方式 A：从 Playlist 批量下载（首选）

```bash
yt-dlp \
  --cookies-from-browser chrome \   # Cookie 认证（解决反爬）
  -x \                               # 仅提取音频
  --audio-format wav \               # 转换为 WAV
  --audio-quality 0 \                # 最高音质
  -o "music_audio/{creator}/%(playlist_index)02d-%(id)s-%(title)s.%(ext)s" \
  "https://www.youtube.com/playlist?list=PLAYLIST_ID"
```

### 方式 B：逐个视频下载（无 Playlist 时）

```bash
# 循环下载多个视频
for id in VIDEO_ID1 VIDEO_ID2 VIDEO_ID3; do
  yt-dlp \
    --cookies-from-browser chrome \
    -x --audio-format wav --audio-quality 0 \
    -o "music_audio/{creator}/%(autonumber)02d-%(id)s-%(title)s.%(ext)s" \
    --autonumber-start 1 \
    "https://www.youtube.com/watch?v=$id"
done
```

> **注意**：方式 B 中 `--autonumber-start 1` 在循环内每次重置，需下载后手动修正序号。

### 方式 C：搜索后下载

```bash
# 1. 先搜索获取 video ID
yt-dlp --cookies-from-browser chrome \
  "ytsearch10:关键词" \
  --flat-playlist --print "%(title)s | %(id)s | %(duration)s"

# 2. 再用方式 B 下载
```

---

## 四、认证问题处理

### Cookie 导出

当遇到 `Sign in to confirm you're not a bot` 错误时：

```bash
# 从 Chrome 导出 cookie（推荐）
--cookies-from-browser chrome

# 备选：手动导出 cookie 文件
--cookies cookies.txt
```

### 速率限制

yt-dlp 自动处理 YouTube 的 `sleep` 要求（通常 4-7 秒间隔），无需额外参数。

---

## 五、后处理

### 修正文件序号（方式 B 余留问题）

```python
import os, glob
mapping = {
    'videoID_1': '01', 'videoID_2': '02', ...
}
for f in sorted(glob.glob('01-*.wav')):
    for vid, num in mapping.items():
        if vid in f:
            os.rename(f, f.replace('01-', f'{num}-', 1))
```

### 验证文件

```bash
ls -lh music_audio/{creator}/
```

---

## 六、文件管理

### .gitignore

```gitignore
# 音频文件不入库（体积大），仅保留 .md / .jsonl 等元数据
*.wav
*.mp3
*.flac
```

### 提交到 Git

```bash
git add music_audio/{creator}/music.md    # 播放列表文档
git add music_audio/{creator}/*.jsonl     # 元数据（可选）
git add music_audio/curated_tracks.md     # 精选汇总
# 不提交 *.wav 文件
```

---

## 七、已下载来源汇总

| 来源 | 目录 | 曲目数 | 下载方式 |
|---|---|---|---|
| Alex-Productions (Audio Library) | `alex-productions/` | 91 首（仅元数据提交） | 方式 A (playlist) |
| LAKEY INSPIRED | `lakey-inspired/` | 12 首 | 方式 A (playlist) |
| Beethoven · Karajan | `beethoven-karajan/` | 9 首 | 方式 B (逐个) |

---

## 八、命令速查

```bash
# 下载 playlist（完整）
yt-dlp --cookies-from-browser chrome -x --audio-format wav --audio-quality 0 \
  -o "DIR/%(playlist_index)02d-%(id)s-%(title)s.%(ext)s" "PLAYLIST_URL"

# 搜索视频
yt-dlp --cookies-from-browser chrome "ytsearch10:关键词" --flat-playlist --print "%(title)s | %(id)s"

# 下载单个视频
yt-dlp --cookies-from-browser chrome -x --audio-format wav --audio-quality 0 \
  -o "DIR/%(id)s-%(title)s.%(ext)s" "VIDEO_URL"
```
