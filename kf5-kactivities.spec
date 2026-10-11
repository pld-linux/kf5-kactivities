#
# Conditional build:
%bcond_with	tests		# test suite

# TODO:
# Conflict /usr/bin/kactivitymanagerd
%define		kdeframever	5.116
%define		kf_ver		%{version}
%define		qt_ver		5.15.2
%define		kfname		kactivities

Summary:	Core components for the KDE's Activities Activity Manager
Summary(pl.UTF-8):	Główne komponenty zarządcy aktywności KDE Activities
Name:		kf5-%{kfname}
Version:	5.116.0
Release:	1
License:	LGPL v2.1+
Group:		X11/Libraries
Source0:	https://download.kde.org/stable/frameworks/%{kdeframever}/%{kfname}-%{version}.tar.xz
# Source0-md5:	303995a8483ad06c9cd7a775691ac610
URL:		https://kde.org/
BuildRequires:	Qt5Core-devel >= %{qt_ver}
BuildRequires:	Qt5DBus-devel >= %{qt_ver}
BuildRequires:	Qt5Gui-devel >= %{qt_ver}
BuildRequires:	Qt5Qml-devel >= %{qt_ver}
BuildRequires:	Qt5Quick-devel >= %{qt_ver}
BuildRequires:	Qt5Sql-devel >= %{qt_ver}
%{?with_tests:BuildRequires:	Qt5Test-devel >= %{qt_ver}}
BuildRequires:	Qt5Widgets-devel >= %{qt_ver}
BuildRequires:	boost-devel >= 1.49
BuildRequires:	cmake >= 3.16
BuildRequires:	gettext-devel
BuildRequires:	kf5-extra-cmake-modules >= %{kf_ver}
BuildRequires:	kf5-kconfig-devel >= %{kf_ver}
BuildRequires:	kf5-kcoreaddons-devel >= %{kf_ver}
%{?with_tests:BuildRequires:	kf5-kwindowsystem-devel >= %{kf_ver}}
BuildRequires:	libstdc++-devel >= 6:4.7
BuildRequires:	ninja
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	Qt5Core >= %{qt_ver}
Requires:	Qt5DBus >= %{qt_ver}
Requires:	Qt5Gui >= %{qt_ver}
Requires:	Qt5Qml >= %{qt_ver}
Requires:	Qt5Quick >= %{qt_ver}
Requires:	Qt5Sql >= %{qt_ver}
Requires:	Qt5Widgets >= %{qt_ver}
Requires:	kf5-dirs
Requires:	kf5-kconfig >= %{kf_ver}
Requires:	kf5-kcoreaddons >= %{kf_ver}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		qt5dir		%{_libdir}/qt5

%description
System service to manage user's activities, track the usage patterns
etc. KActivities library API for using and interacting with the
Activity Manager as a consumer, application adding information to them
or as an activity manager. Workspace Plugins for KDE workspace to
easier integrate activities (KIO, etc.)

%description -l pl.UTF-8
Usługa systemowa do zarządzania aktywnościami użytkowników, śledzenia
wzorców użycia itp., biblioteka KActivities do używania i
współpracy z zarządcą aktywności w roli konsumenta, aplikacja dodająca
informacje do konsumentów lub zarządcy aktywności oraz wtyczki
środowiska roboczego KDE ułatwiające integrację aktywności (KIO itp.).

%package devel
Summary:	Header files for %{kfname} development
Summary(pl.UTF-8):	Pliki nagłówkowe dla programistów używających %{kfname}
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	Qt5Core-devel >= %{qt_ver}
Requires:	Qt5DBus-devel >= %{qt_ver}
Requires:	libstdc++-devel >= 6:4.7

%description devel
Header files for %{kfname} development.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla programistów używających %{kfname}.

%prep
%setup -q -n %{kfname}-%{version}

%build
%cmake -B build \
	-G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON

%ninja_build -C build

%if %{with tests}
%ninja_build -C build test
%endif

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc MAINTAINER README.md
%attr(755,root,root) %{_bindir}/kactivities-cli
%{_libdir}/libKF5Activities.so.*.*.*
%ghost %{_libdir}/libKF5Activities.so.5
%dir %{qt5dir}/qml/org/kde/activities
%{qt5dir}/qml/org/kde/activities/libkactivitiesextensionplugin.so
%{qt5dir}/qml/org/kde/activities/qmldir
%{_datadir}/qlogging-categories5/kactivities.categories
%{_datadir}/qlogging-categories5/kactivities.renamecategories

%files devel
%defattr(644,root,root,755)
%{_libdir}/libKF5Activities.so
%{_includedir}/KF5/KActivities
%{_libdir}/cmake/KF5Activities
%{_pkgconfigdir}/libKActivities.pc
%{qt5dir}/mkspecs/modules/qt_KActivities.pri
