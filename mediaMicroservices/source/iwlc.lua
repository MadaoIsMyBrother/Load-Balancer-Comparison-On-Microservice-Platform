local _iwlc = {}
local mt = { __index = _iwlc }

local Node = require("nodes")

function _iwlc.new(_, hosts, weights, C)
    local self = {
        nodes = {},
        conn_dict = {},
        least = 1,
        old_s = -1,
        C = C,
        flag = 0,
        count = 1,
        conns = -1
    }
    for i, host in ipairs(hosts) do
        new_node = Node.new(_,host, weights[i])
        table.insert(self.nodes, new_node)
    end
    return setmetatable(self, mt)
end

function _iwlc.get_connections(self, name)
    local concat = table.concat
    local upstream = require "ngx.upstream"
    local get_servers = upstream.get_servers
    local get_upstreams = upstream.get_upstreams
    local get_primary_peers = upstream.get_primary_peers
    local us = get_upstreams()
    local current_host = name
    for _, u in ipairs(us) do
        local srvs, err = get_primary_peers(u)
        if not srvs then
            ngx.say("failed to get servers in upstream ", u)
        else
            for _, srv in ipairs(srvs) do
                local current_host = srv.name
                if (current_host == name) then
                    return srv.conns
                end
            end
        end
    end
end

function _iwlc.overload(self, s, n)
    if (self.flag == 1) then
        self.count = self.count-1
        if (self.count < 1) then
            self.nodes[self.old_s].flag = true
            self.flag = 0
        end
        return
    end
    if (n < 2) then
        return
    end
    if (self.old_s ~= s) then
        self.old_s = s
        self.count = 1
        return
    end
    self.count = self.count + 1
    if (self.count >= self.C) then
        self.count = self.C - 1
        self.nodes[self.old_s].flag = false
        self.flag = 1
    end
end


function _iwlc.iwlc(self, one, two, three)
    local active = 0
    self.nodes[1].conns = one
    self.nodes[2].conns = two
    self.nodes[3].conns = three
    local least_connections = self.nodes[self.least].conns
    local least_weight = self.nodes[self.least].weight
    local n=3
    for i=1, n do
        if (self.nodes[i].flag == false) then
            ::continue::
        end
        if (self.least == i) then
            ::continue::
        end
        if (least_connections / least_weight > self.nodes[i].conns / self.nodes[i].weight) then
            self.least = i
        end
        active = active + 1
    end
    self:overload(self.least, active)
    return self.nodes[self.least].host
end

return _iwlc