Summary:	Advanced panel tool
Summary(pl):	Zaawansowane zarz±dzanie panelami
Name:		mozilla-addon-multizilla
%define		_realname	multiviews
%define	bver	1.1.15
Version:	%{bver}beta2
%define	fver	%(echo %{bver} | tr -d .)
Release:	1
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://downloads.mozdev.org/multizilla/%{_realname}-v%{fver}.xpi
Source1:	%{_realname}-installed-chrome.txt
URL:		http://multizilla.mozdev.org/
BuildRequires:	unzip
Requires:	mozilla >= 1.0
BuildRoot:	%{tmpdir}/%{_realname}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_chromedir	%{_libdir}/mozilla/chrome

%description
Multizilla is a tool to maintain panels - closing them, opening,
saving their status between sessions. It contains additional toolbar.

%description -l pl
Narzêdzie do zarz±dzania panelami, u³atwiaj±ce zamykanie, otwieranie
paneli oraz zapisywanie ich statusu pomiêdzy sesjami. Zawiera
dodatkowy pasek narzêdziowy.

%prep

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_chromedir}

unzip %{SOURCE0} -d $RPM_BUILD_ROOT%{_chromedir}
install %{SOURCE1} $RPM_BUILD_ROOT%{_chromedir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
cd %{_chromedir}
cat %{_realname}-installed-chrome.txt >> installed-chrome.txt

%postun
cd %{_chromedir}
cat installed-chrome.txt | grep -v "%{_realname}" > installed-chrome.txt.tmp
cat installed-chrome.txt.tmp > installed-chrome.txt
rm -f installed-chrome.txt.tmp

%files
%defattr(644,root,root,755)
%{_chromedir}/%{_realname}.jar
%{_chromedir}/%{_realname}-installed-chrome.txt
