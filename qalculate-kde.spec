Summary:	A multi-purpose desktop calculator for GNU/Linux
Summary(pl):	Wielozadaniowy kalkulator dla systemu GNU/Linux
Name:		qalculate-kde
Version:	0.9.4
Release:	0.1
License:	GPL
Group:		Applications/Engineering
Source0:	http://dl.sourceforge.net/qalculate/%{name}-%{version}.tar.gz
# Source0-md5:	ec11bf96f181d6eb3ad1ddc430388701
URL:		http://qalculate.sourceforge.net/
BuildRequires:	cln-devel >= 1.1.0
BuildRequires:	gettext
BuildRequires:	glib2-devel
BuildRequires:	kdelibs-devel
BuildRequires:	libqalculate-devel
BuildRequires:	libxml2-devel
BuildRequires:	rpmbuild(macros) >= 1.129
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
%configure \
	--disable-rpath

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_desktopdir}

%{__make} install \
        kde_htmldir=%{_kdedocdir} \
	DESTDIR=$RPM_BUILD_ROOT

mv -f $RPM_BUILD_ROOT{%{_datadir}/applnk/Utilities,%{_desktopdir}}/qalculate_kde.desktop

%find_lang qalculate_kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f qalculate_kde.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog COPYING
%attr(755,root,root) %{_bindir}/qalculate-kde
%{_iconsdir}/hicolor/*/apps/*
%{_iconsdir}/hicolor/32x32/actions/qalculate_convert.png
%{_desktopdir}/*
%{_datadir}/apps/qalculate_kde/qalculate_kdeui.rc
%{_docdir}/kde/HTML/en/qalculate_kde/*
