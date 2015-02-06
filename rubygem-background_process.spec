%define oname background_process

Name:       rubygem-%{oname}
Version:    1.2
Release:    4
Summary:    A library for spawning and interacting with UNIX processes
Group:      Development/Ruby
License:    MIT
URL:        http://github.com/timcharper/background_process
Source0:    http://rubygems.org/gems/%{oname}-%{version}.gem
Requires:   rubygems
BuildRequires: rubygems
BuildArch:  noarch
Provides:   rubygem(%{oname}) = %{version}

%description
A library for spawning and interacting with UNIX processes


%prep

%build

%install
mkdir -p %{buildroot}%{gem_dir}
gem install --local --install-dir %{buildroot}%{gem_dir} \
            --force --rdoc %{SOURCE0}

%clean

%files
%defattr(-, root, root, -)
%dir %{gem_dir}/gems/%{oname}-%{version}/
%{gem_dir}/gems/%{oname}-%{version}/lib/
%{gem_dir}/gems/%{oname}-%{version}/spec/
%doc %{gem_dir}/doc/%{oname}-%{version}
%doc %{gem_dir}/gems/%{oname}-%{version}/MIT-LICENSE
%doc %{gem_dir}/gems/%{oname}-%{version}/README.textile
%{gem_dir}/cache/%{oname}-%{version}.gem
%{gem_dir}/specifications/%{oname}-%{version}.gemspec


