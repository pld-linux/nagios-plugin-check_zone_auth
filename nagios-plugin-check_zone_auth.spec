%define		plugin	check_zone_auth
%include	/usr/lib/rpm/macros.perl
Summary:	Nagios plugin to check authoritative nameservers being in sync
Name:		nagios-plugin-%{plugin}
Version:	1.13
Release:	1
License:	BSD-like
Group:		Networking
Source0:	http://dns.measurement-factory.com/tools/nagios-plugins/src/check_zone_auth
# Source0-md5:	cd9d07621cc2baf8714c88579da64ff5
Source1:	%{plugin}.cfg
URL:		http://dns.measurement-factory.com/tools/nagios-plugins/check_zone_auth.html
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	nagios-common
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/nagios/plugins
%define		plugindir	%{_prefix}/lib/nagios/plugins

%description
Use this plugin with Nagios to make sure that the authoritative
nameservers for a given zone remain in sync.

%prep
%setup -qcT
cp -p %{SOURCE0} %{plugin}

grep -q '%{plugin},v %{version} ' %{plugin}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir},%{plugindir}}
install -p %{plugin} $RPM_BUILD_ROOT%{plugindir}/%{plugin}
cp -a %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/%{plugin}.cfg

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(640,root,nagios) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{plugin}.cfg
%attr(755,root,root) %{plugindir}/%{plugin}
