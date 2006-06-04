Summary:	A multi-purpose desktop calculator for GNU/Linux
Name:		qalculate-kde
Version:	0.9.4
Release:	0.1
License:	GPL
Group:		Applications/Engineering
URL:		http://qalculate.sourceforge.net/
Source0:	http://dl.sourceforge.net/qalculate/%{name}-%{version}.tar.gz
# Source0-md5:	ec11bf96f181d6eb3ad1ddc430388701
BuildRequires:	gettext
BuildRequires:	kdelibs-devel
BuildRequires:	libqalculate-devel
Requires:	gnuplot
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Qalculate! is a modern multi-purpose desktop calculator for GNU/Linux.
It is small and simple to use but with much power and versatility
underneath. Features include customizable functions, units, arbitrary
precision, plotting.

This package provides a QT/KDE graphical interface for Qalculate!

%prep
%setup -q

%build
#unset QTDIR || : ; . %{_sysconfdir}/profile.d/qt.sh
#export QTLIB=${QTDIR}/lib QTINC=${QTDIR}/include
%configure \
	--disable-rpath

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
        kde_htmldir=%{_kdedocdir} \
	DESTDIR=$RPM_BUILD_ROOT

#%find_lang %{name}_kde
# --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
# -f %{name}.lang
%doc AUTHORS ChangeLog COPYING
%attr(755,root,root) %{_bindir}/qalculate-kde
%{_iconsdir}/hicolor/*/apps/*
%{_iconsdir}/hicolor/32x32/actions/qalculate_convert.png
%{_datadir}/applnk/Utilities/qalculate_kde.desktop
%{_datadir}/apps/qalculate_kde/qalculate_kdeui.rc
%{_docdir}/kde/HTML/en/qalculate_kde/*
#   /usr/share/locale/nl/LC_MESSAGES/qalculate_kde.mo
#   /usr/share/locale/sv/LC_MESSAGES/qalculate_kde.mo

#%{_datadir}/locale/sv/LC_MESSAGES/qalculate_kde.mo # FIXME consider using %find_lang
