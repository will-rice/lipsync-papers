-- Clean pandoc's reading of arXiv's LaTeXML HTML for GitHub markdown.

-- LaTeXML lays out numbered equations as tables. Pandoc would write them as
-- pipe tables wrapping a math fence, which GitHub cannot render, so each
-- equation row becomes display math with its number as a \tag.
function Table(table_)
  if not table_.classes:includes("ltx_eqn_table") then
    return nil
  end
  local equations = {}
  for _, body in ipairs(table_.bodies) do
    for _, row in ipairs(body.body) do
      local parts, number = {}, nil
      for _, cell in ipairs(row.cells) do
        pandoc.Blocks(cell.contents):walk({
          Math = function(math)
            table.insert(parts, math.text)
          end,
          Str = function(str)
            number = str.text:match("^%((.+)%)$") or number
          end,
        })
      end
      if #parts > 0 then
        local tex = table.concat(parts, " ")
        if number then
          tex = tex .. " \\tag{" .. number .. "}"
        end
        table.insert(equations, pandoc.Para({ pandoc.Math("DisplayMath", tex) }))
      end
    end
  end
  return equations
end

-- Anchors inside the arXiv page do not exist in the markdown, and titles
-- carry arXiv's section breadcrumbs.
function Link(link)
  if link.target:sub(1, 1) == "#" then
    return link.content
  end
  link.title = ""
  return link
end

-- LaTeXML's placeholder alt text; the figure caption follows the image.
function Image(image)
  if pandoc.utils.stringify(image.caption) == "Refer to caption" then
    image.caption = {}
  end
  return image
end
