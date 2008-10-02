%define SourceDir 2008_0708_RT2860_Linux_STA_v1.7.0.0

Name:           rt2860
Version:        1.7.0
Release:        3%{?dist}
Summary:        Common files for RaLink 802.11 rt2860 driver

Group:          System Environment/Kernel
License:        GPLv2+
URL:            http://www.ralinktech.com/
Source0:        http://www.ralinktech.com.tw/data/drivers/%{SourceDir}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch

Provides:       %{name}-kmod-common = %{version}-%{release}
Requires:       %{name}-kmod >= %{version}

%description
This package contains the documentation and configuration files for the Ralink
Driver for WiFi, a linux device driver for 802.11a/b/g universal NIC cards - 
either PCI, PCIe or MiniPCI - that use Ralink chipsets (rt2760, rt2790, rt2860,
rt2890).


%prep
%setup -q -c


%build
echo "Nothing to build"


%install
rm -rf $RPM_BUILD_ROOT
install -D -p -m 0644 %{SourceDir}/RT2860STA.dat $RPM_BUILD_ROOT/etc/Wireless/RT2860STA.dat


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc %{SourceDir}/README_STA %{SourceDir}/iwpriv_usage.txt
/etc/Wireless


%changelog
* Thu Oct 02 2008 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info - 1.7.0-3
- rebuild for rpm fusion

* Fri Sep 14 2008 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> 1.7.0-2
- own /etc/Wireless (nothing else in Fedora owns it)
- License is GPLv2+ 

* Fri Sep 05 2008 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> 1.7.0-1
- Initial Version based on rt2860-kmod as submitted by James Bottomley
