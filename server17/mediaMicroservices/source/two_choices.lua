local _two_choices = {}
local mt = { __index = _two_choices }

function poisson(lam)
    local el = math.exp(-lam)
    local n = 0
    local u =  math.random()
    local pp = el
    local fact = 1
    local pow = 1
    while (u > pp) do
        n = n+1
        fact = n*fact
        pow = lam * pow
        pp = pp + (pow/fact)*el
    end
    return n
end

function _two_choices.new(_, hosts)
    local self = {
        nodes = {},
        rates = {},
        dists = {},
        loads = {},
        idx = 1
    }
    local n = 15000
    for i=1,n do
        table.insert(self.nodes, hosts[i])
    end
    for i=1,n do
        table.insert(self.rates, poisson(0.99))
    end
    for i=1,n do
        table.insert(self.dists, self.rates[i]*0.1+1)
    end
    for i=1,n do
        table.insert(self.loads, 0)
    end
    math.randomseed(os.time())
    return setmetatable(self, mt)
end

function _two_choices.find(self)
    local n = #(self.nodes)
    local choice_one = math.random(1, n)
    local choice_two = math.random(1, n)
    local best_choice = ''
    if self.loads[choice_one] < self.loads[choice_two] then
        best_choice = choice_one
    else
        best_choice = choice_two
    end
    local weight = self.dists[self.idx]
    self.idx = self.idx+1
    self.loads[best_choice] = self.loads[best_choice] + weight
    return self.nodes[best_choice]
end

return _two_choices
