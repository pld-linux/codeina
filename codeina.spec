Summary:	Codec search and installation helper
Summary(pl.UTF-8):	Pomocnik do szukania i instalcji kodeków
Name:		codeina
Version:	0.10.6
Release:	0.1
License:	GPL
Group:		Applications/Multimedia
Source0:	http://core.fluendo.com/gstreamer/src/codeina/%{name}-%{version}.tar.bz2
# Source0-md5:	8084a95721d3be28e81e240543789e80
Patch0:		%{name}-no_python_2.5.patch
Patch1:		%{name}-python_prefix.patch
URL:		https://core.fluendo.com/gstreamer/trac/wiki/codeina
BuildRequires:	python-PyYAML
BuildRequires:	python-gnome-extras-mozilla
BuildRequires:	python-pynotify
Requires:	python >= 2.5
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Codeina installs missing codecs on your machine. Codeina is run by other
applications, such as Totem or Rhythmbox, when no plugin has been found to
decode a given file. Based on the characteristics of these files, Codeina
searches a plugin amongst the available ones, and propose the matching
packages for installation.

%description -l pl.UTF-8
Codeina instaluje brakujące kodeki w Twoim systemie. Uruchamiana jest przez
inne aplikacje, takie jak Totem lub Rhythmbox, gdy nie mogą one znaleźć
kodeka niezbędnego do odtworzenia pliku multimedialnego. Na podstawie opisu
pliku Codeina szuka pasujących wtyczek w Internecie i proponuje instalację
pasujących pakietów.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
PYNOTIFY_LIBS=" " PYNOTIFY_CFLAGS=" " %configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS COPYING NEWS README
%attr(755,root,root) %dir %{_sysconfdir}/%{name}
%attr(755,root,root) %dir %{_sysconfdir}/%{name}/providers
%attr(644,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}/*.xml
%attr(644,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}/providers/*
%{_sysconfdir}/xdg/autostart/%{name}-update.desktop
%attr(755,root,root) %{_bindir}/%{name}
%attr(755,root,root) %{_bindir}/%{name}.bin
%{_datadir}/%{name}
%{py_sitedir}/%{name}
%{_desktopdir}/%{name}.desktop
