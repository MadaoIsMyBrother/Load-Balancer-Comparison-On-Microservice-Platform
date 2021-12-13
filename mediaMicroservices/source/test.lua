-- local IWLC = require("iwlc")
-- local test = IWLC.new(_, {"172.22.154.16:8080", "172.22.154.20:8080"}, {1,2}, 2)


-- print(test:iwlc(2))
-- print(test:iwlc(2))
-- print(test:iwlc(2))
-- print(test:iwlc(2))
-- print(test:iwlc(2))local Node = require("nodes")
-- local a = Node.new(_, "abcd", 100)
-- print(a.host, a.port, a.weight)
-- local m_array = {}
-- m_array:insert(a)
-- print(m_array[0].flag)
-- local Node = require("nodes")
-- local a = Node.new(_, "abcd", 100)
-- print(a.host, a.port, a.weight)
-- local m_array = {}
-- table.insert(m_array, a)
-- print(m_array[1].flag)
local TWO_CHOICE = require("two_choice")
local a = TWO_CHOICE.new(_, {"172.22.154.16:8080", "172.22.154.20:8080"})
for i=1,10 do 
    print(a:find(), "\n")
end