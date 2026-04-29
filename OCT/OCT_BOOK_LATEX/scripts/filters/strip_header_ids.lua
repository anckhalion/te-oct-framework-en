function Header(el)
  if el.identifier and el.identifier ~= "" then
    el.identifier = ""
  end
  return el
end
