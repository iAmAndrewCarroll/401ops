-- SimpleInfo.nse
-- Script Name:                  Simple Information Gathering Script
-- Author:                       Andrew Carroll
-- Date of latest revision:      03/02/2024
-- Purpose:                      Gathers basic information about a target host.

description = [[
Gathers basic information about a target host.
]]

author = "Andrew Carroll"
license = "Same as Nmap--See https://nmap.org/book/man-legal.html"
categories = {"default", "safe"}

portrule = function(host, port)
    -- The portrule should return true if the script should run on the given host/port pair.
    -- For simplicity, we will just return true to run on all hosts and ports provided to Nmap.
    return true
end

action = function(host, port)
    -- Check if the host or port is nil
    if not host or not port then
        return "Invalid host or port"
    end

    -- Check if the port state is nil
    if not port.state then
        return "Port state is nil"
    end

    -- Retrieve the hostname if available
    local hostname = host.hostname or "Unknown"

    -- The action function performs the actual work of the script and returns the result as a string.
    local host_ip = host.ip or "n/a"
    local port_status = (port.state == "open") and "Open" or "Closed"

    -- Format the output with additional information
    local output = string.format("Host: %s (%s)\nIP: %s\nPort %s: %s\n", hostname, host_ip, host_ip, port.number, port_status)

    return output
end

