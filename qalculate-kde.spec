Summary:	A multi-purpose desktop calculator for GNU/Linux
Summary(pl.UTF-8):	Wielozadaniowy kalkulator dla systemu GNU/Linux
Name:		qalculate-kde
Version:	0.9.5
Release:	1
License:	GPL
Group:		Applications/Engineering
Source0:	http://dl.sourceforge.net/qalculate/%{name}-%{version}.tar.gz
# Source0-md5:	46eb26a6e33fbc65581c2020cf187f4e
URL:		http://qalculate.sourceforge.net/
BuildRequires:	cln-devel >= 1.1.0
BuildRequires:	gettext
BuildRequires:	glib2-devel >= 2.0
BuildRequires:	kdelibs-devel
BuildRequires:	libqalculate-devel >= 0.9.4
BuildRequires:	libxml2-devel >= 2.0
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.129
Requires:	gnuplot
Requires:	libqalculate >= 0.9.4
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
%configure \
	--disable-rpath

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_desktopdir}

%{__make} install \
        kde_htmldir=%{_kdedocdir} \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang qalculate_kde --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f qalculate_kde.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog
%attr(755,root,root) %{_bindir}/qalculate-kde
%{_iconsdir}/hicolor/*/apps/*
%{_iconsdir}/hicolor/32x32/actions/qalculate_convert.png
%{_desktopdir}/kde/*.desktop
%dir %{_datadir}/apps/qalculate_kde
%{_datadir}/apps/qalculate_kde/qalculate_kdeui.rc
