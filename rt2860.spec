Name:		rt2860
Version:	2.3.0.0
Release:	1%{?dist}
Summary:	Common files for RaLink 802.11 rt2860 driver
Group:		System Environment/Kernel
License:	GPLv2+
URL:		http://www.ralinktech.com/support.php?s=2
# No direct links anymore. See the above URL
Source0:	2010_01_29_RT2860_Linux_STA_v2.3.0.0.tar.bz2
Source1:	ReleaseNote_RT2860.txt
# To suspend properly (RPMFusion BZ#199)
Source2:	suspend.sh
Source3:	blacklist-rt2800pci.conf
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:	noarch
Provides:	%{name}-kmod-common = %{version}
Requires:	%{name}-kmod >= %{version}

%description
This package contains the documentation and configuration files for the Ralink
Driver for WiFi, a Linux device driver for 802.11a/b/g universal NIC cards -
either PCI, PCIe or MiniPCI - that use Ralink chipsets (rt2760, rt2790, rt2860,
rt2890).

%prep
%setup -q -n 2010_01_29_RT2860_Linux_STA_v2.3.0.0

sed 's/\r//' %{SOURCE1} > ./ReleaseNotes
touch -r %{SOURCE1} ./ReleaseNotes
iconv -f JOHAB -t UTF8 README_STA -o README_STA.tmp
touch -r README_STA README_STA.tmp
mv -f README_STA.tmp README_STA
sed 's/\r//' sta_ate_iwpriv_usage.txt > sta_ate_iwpriv_usage.txt.tmp
iconv -f JOHAB -t UTF8 sta_ate_iwpriv_usage.txt.tmp -o sta_ate_iwpriv_usage.txt.tmp2
touch -r sta_ate_iwpriv_usage.txt sta_ate_iwpriv_usage.txt.tmp2
mv -f sta_ate_iwpriv_usage.txt.tmp2 sta_ate_iwpriv_usage.txt

%build
# Needed for WPA2 support (RFBZ #664)
sed -i 's|HT_DisallowTKIP=1|HT_DisallowTKIP=0|' RT2860STA.dat
sleep 1m

%install
rm -rf $RPM_BUILD_ROOT
# buildsys sometimes fails without this:
sleep 1m
install -dm 755 $RPM_BUILD_ROOT/%{_sysconfdir}/Wireless/RT2860STA
install -pm 0644 RT2860STA*.dat $RPM_BUILD_ROOT/%{_sysconfdir}/Wireless/RT2860STA/

cp -a %{SOURCE2} .
install -dm 755 $RPM_BUILD_ROOT/%{_sysconfdir}/modprobe.d/
cp -a %{SOURCE3} $RPM_BUILD_ROOT/%{_sysconfdir}/modprobe.d/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc ReleaseNotes README_STA *iwpriv_usage.txt suspend.sh
%dir %{_sysconfdir}/Wireless
%dir %{_sysconfdir}/Wireless/RT2860STA
%config(noreplace) %{_sysconfdir}/Wireless/RT2860STA/RT2860STA*.dat
%config(noreplace) %{_sysconfdir}/modprobe.d/blacklist-rt2800pci.conf

%changelog
* Thu Apr 22 2010 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 2.3.0.0-1
- version update (2.3.0.0)

* Wed Dec 09 2009 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 2.1.2.0-3
- Blacklist kernel's rt2800pci module

* Wed Jun 17 2009 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 2.1.2.0-2
- Modify RT2860STA.dat to support WPA2 (RFBZ #664)

* Sat May 23 2009 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 2.1.2.0-1
- version update (2.1.2.0)

* Sat Apr 24 2009 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 2.1.1.0-1
- version update (2.1.1.0)

* Mon Apr 20 2009 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> - 2.1.0.0-1
- version update (2.1.0.0)

* Sun Mar 29 2009 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 1.8.0.0-3
- rebuild for new F11 features

* Tue Mar 10 2009 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> - 1.8.0.0-2
- Add suspend script (RPMFusion BZ#199)

* Sat Oct 19 2008 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> - 1.8.0.0-1
- Version update (1.8.0.0)

* Thu Oct 02 2008 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 1.7.0-3
- rebuild for rpm fusion

* Fri Sep 14 2008 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> 1.7.0-2
- own /etc/Wireless (nothing else in Fedora owns it)
- License is GPLv2+

* Fri Sep 05 2008 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> 1.7.0-1
- Initial Version based on rt2860-kmod as submitted by James Bottomley
