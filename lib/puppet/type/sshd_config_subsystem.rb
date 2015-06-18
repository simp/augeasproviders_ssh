# Manages Subsystem settings in OpenSSH's sshd_config file
#
# Copyright (c) 2012 Raphaël Pinson
# Licensed under the Apache License, Version 2.0

Puppet::Type.newtype(:sshd_config_subsystem) do
  @doc = "Manages Subsystem settings in an OpenSSH sshd_config file."

  ensurable

  def initialize(args)
    super(args)

    if self[:notify] then
      self[:notify] += ['Service[sshd]']
    else
      self[:notify] = ['Service[sshd]']
    end
  end

  newparam(:name) do
    desc "The name of the subsystem to set."
    isnamevar
  end

  newproperty(:command) do
    desc "The command to execute upon subsystem request."
  end

  newparam(:target) do
    desc "The file in which to store the settings, defaults to
      `/etc/ssh/sshd_config`."
  end

  autorequire(:file) do
    self[:target]
  end
end
