%define oname background_process

Name:       rubygem-%{oname}
Version:    1.2
Release:    %mkrel 1
Summary:    A library for spawning and interacting with UNIX processes
Group:      Development/Ruby
License:    MIT
URL:        http://github.com/timcharper/background_process
Source0:    http://rubygems.org/gems/%{oname}-%{version}.gem
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-root
Requires:   rubygems
BuildRequires: rubygems
BuildArch:  noarch
Provides:   rubygem(%{oname}) = %{version}

%description
A library for spawning and interacting with UNIX processes


%prep

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{ruby_gemdir}
gem install --local --install-dir %{buildroot}%{ruby_gemdir} \
            --force --rdoc %{SOURCE0}

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, -)
%dir %{ruby_gemdir}/gems/%{oname}-%{version}/
%{ruby_gemdir}/gems/%{oname}-%{version}/lib/
%{ruby_gemdir}/gems/%{oname}-%{version}/spec/
%doc %{ruby_gemdir}/doc/%{oname}-%{version}
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/MIT-LICENSE
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/README.textile
%{ruby_gemdir}/cache/%{oname}-%{version}.gem
%{ruby_gemdir}/specifications/%{oname}-%{version}.gemspec


%changelog
* Thu Dec 02 2010 Rémy Clouard <shikamaru@mandriva.org> 1.2-1mdv2011.0
+ Revision: 605350
- import rubygem-background_process

