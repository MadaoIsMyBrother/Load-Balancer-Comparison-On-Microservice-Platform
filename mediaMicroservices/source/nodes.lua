local Node = {}
local mt = { __index = Node }
local upstream = require "ngx.upstream"
local get_servers = upstream.get_servers
local get_upstreams = upstream.get_upstreams
local get_primary_peers = upstream.get_primary_peers
function Node:new(host, weight)
    local self = {
        flag = false,
        conns = 0,
        host = host,
        weight = weight
    }
    return setmetatable(self,mt)
end

function Node:get_conn()
    local us = get_upstreams()
    for _, u in ipairs(us) do
        local srvs, err = get_primary_peers(u)
        if not srvs then
            ngx.say("failed to get servers in upstream ", u)
        else
            for _, srv in ipairs(srvs) do
                local current_host = srv.name
                if (current_host == current_host) then
                    return srv.conns
                end
            end
        end
    end
    return -1
end


return Node