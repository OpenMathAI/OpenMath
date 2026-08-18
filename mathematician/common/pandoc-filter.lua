
-- 去掉所有 RawBlock/RawInline(html) 节点，避免 LaTeX 报错
function RawBlock(el)
  if el.format == "html" then return {} end
  return nil
end
function RawInline(el)
  if el.format == "html" then return {} end
  return nil
end

-- 把没有 src 的 Image 去掉；把 http(s) 图片 src 保留，稍后 Python 会替换
function Image(img)
  if not img.src or img.src == "" then return {} end
  return img
end

-- 把空的段落去掉
function Para(p)
  if #p.content == 0 then return {} end
  return nil
end

-- 去掉脚注里的 href "Cite note" 等噪声
function Note(n)
  return {}
end
