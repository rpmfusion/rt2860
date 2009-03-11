%define SourceName 2008_0918_RT2860_Linux_STA_v1.8.0.0

Name:		rt2860
Version:	1.8.0.0
Release:	2%{?dist}
Summary:	Common files for RaLink 802.11 rt2860 driver
Group:		System Environment/Kernel
License:	GPLv2+
URL:		http://www.ralinktech.com/ralink/Home/Support/Linux.html
Source0:	http://www.ralinktech.com.tw/data/drivers/%{SourceName}.tar.bz2
Source1:	http://www.ralinktech.com.tw/data/drivers/ReleaseNote-RT2860.txt
# To suspend properly (RPMFusion BZ#199)
Source2:	suspend.sh
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:	noarch
Provides:	%{name}-kmod-common = %{version}
Requires:	%{name}-kmod >= %{version}

%description
This package contains the documentation and configuration files for the Ralink
Driver for WiFi, a linux device driver for 802.11a/b/g universal NIC cards -
either PCI, PCIe or MiniPCI - that use Ralink chipsets (rt2760, rt2790, rt2860,
rt2890).

%prep
%setup -q -n %{SourceName}
iconv -f JOHAB -t UTF8 %{SOURCE1} -o ./ReleaseNotes
sed -i 's/\r//' ./ReleaseNotes
iconv -f JOHAB -t UTF8 README_STA -o README_STA
sed -i 's/\r//' README_STA

%build
echo "Nothing to build."

%install
rm -rf $RPM_BUILD_ROOT
install -dm 755 $RPM_BUILD_ROOT/%{_sysconfdir}/Wireless/RT2860STA
install -pm 0644 RT2860STA.dat $RPM_BUILD_ROOT/%{_sysconfdir}/Wireless/RT2860STA/

install -dm 755 $RPM_BUILD_ROOT/%{_datadir}/%{name}
install -pm 0755 %{SOURCE2} $RPM_BUILD_ROOT/%{_datadir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc ReleaseNotes README_STA iwpriv_usage.txt
%dir %{_sysconfdir}/Wireless
%dir %{_sysconfdir}/Wireless/RT2860STA
%config(noreplace) %{_sysconfdir}/Wireless/RT2860STA/RT2860STA.dat
%{_datadir}/%{name}

%changelog
* Tue Mar 10 2009 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> - 1.8.0.0-2
- Add suspend script (RPMFusion BZ#199)

* Sat Oct 19 2008 Orcan Ogetbil  <oget[DOT]fedora[AT]gmail[DOT]com> - 1.8.0.0-1
- Version update (1.8.0.0)

* Thu Oct 02 2008 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 1.7.0-3
- rebuild for rpm fusion

* Fri Sep 14 2008 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> 1.7.0-2
- own /etc/Wireless (nothing else in Fedora owns it)
- License is GPLv2+

* Fri Sep 05 2008 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> 1.7.0-1
- Initial Version based on rt2860-kmod as submitted by James Bottomley
