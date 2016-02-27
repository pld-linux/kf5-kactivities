# TODO:
# Conflict /usr/bin/kactivitymanagerd
%define		kdeframever	5.19
%define		qtver		5.3.2
%define		kfname		kactivities

Summary:	Core components for the KDE's Activities Activity Manager
Name:		kf5-%{kfname}
Version:	5.19.0
Release:	1
License:	LGPL v2.1+
Group:		X11/Libraries
Source0:	http://download.kde.org/stable/frameworks/%{kdeframever}/%{kfname}-%{version}.tar.xz
# Source0-md5:	b5ceb59e0b354858849c6728d7df2c3d
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5DBus-devel >= %{qtver}
BuildRequires:	Qt5Gui-devel >= %{qtver}
BuildRequires:	Qt5Network-devel >= %{qtver}
BuildRequires:	Qt5Qml-devel >= %{qtver}
BuildRequires:	Qt5Sql-devel >= %{qtver}
BuildRequires:	Qt5Test-devel >= %{qtver}
BuildRequires:	Qt5Widgets-devel >= %{qtver}
BuildRequires:	Qt5Xml-devel >= %{qtver}
BuildRequires:	boost-devel
BuildRequires:	cmake >= 2.8.12
BuildRequires:	gettext-devel
BuildRequires:	kf5-attica-devel >= %{version}
BuildRequires:	kf5-extra-cmake-modules >= 1.4.0
BuildRequires:	kf5-kauth-devel >= %{version}
BuildRequires:	kf5-kbookmarks-devel >= %{version}
BuildRequires:	kf5-kcmutils-devel >= %{version}
BuildRequires:	kf5-kcodecs-devel >= %{version}
BuildRequires:	kf5-kcompletion-devel >= %{version}
BuildRequires:	kf5-kconfig-devel >= %{version}
BuildRequires:	kf5-kconfigwidgets-devel >= %{version}
BuildRequires:	kf5-kcoreaddons-devel >= %{version}
BuildRequires:	kf5-kdbusaddons-devel >= %{version}
BuildRequires:	kf5-kdeclarative-devel >= %{version}
BuildRequires:	kf5-kglobalaccel-devel >= %{version}
BuildRequires:	kf5-kguiaddons-devel >= %{version}
BuildRequires:	kf5-ki18n-devel >= %{version}
BuildRequires:	kf5-kiconthemes-devel >= %{version}
BuildRequires:	kf5-kio-devel >= %{version}
BuildRequires:	kf5-kitemviews-devel >= %{version}
BuildRequires:	kf5-kjobwidgets-devel >= %{version}
BuildRequires:	kf5-kservice-devel >= %{version}
BuildRequires:	kf5-ktextwidgets-devel >= %{version}
BuildRequires:	kf5-kwidgetsaddons-devel >= %{version}
BuildRequires:	kf5-kwindowsystem-devel >= %{version}
BuildRequires:	kf5-kxmlgui-devel >= %{version}
BuildRequires:	kf5-solid-devel >= %{version}
BuildRequires:	kf5-sonnet-devel >= %{version}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		qt5dir		%{_libdir}/qt5

%description
System service to manage user's activities, track the usage patterns
etc. KActivities library API for using and interacting with the
Activity Manager as a consumer, application adding information to them
or as an activity manager. Workspace Plugins for KDE workspace to
easier integrate activities (KIO, etc.)

%package devel
Summary:	Header files for %{kfname} development
Summary(pl.UTF-8):	Pliki nagłówkowe dla programistów używających %{kfname}
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for %{kfname} development.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla programistów używających %{kfname}.

%prep
%setup -q -n %{kfname}-%{version}

%build
install -d build
cd build
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	../
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build/ install \
        DESTDIR=$RPM_BUILD_ROOT

%find_lang %{kfname}5

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f %{kfname}5.lang
%defattr(644,root,root,755)
%doc README.md
%attr(755,root,root) %{_bindir}/kactivitymanagerd
%attr(755,root,root) %ghost %{_libdir}/libKF5Activities.so.5
%attr(755,root,root) %{_libdir}/libKF5Activities.so.*.*
%attr(755,root,root) %{_libdir}/libkactivitymanagerd_plugin.so
%attr(755,root,root) %{qt5dir}/plugins/kactivitymanagerd_fileitem_linking_plugin.so
%dir %{qt5dir}/plugins/kactivitymanagerd
%dir %{qt5dir}/plugins/kactivitymanagerd/1
%attr(755,root,root) %{qt5dir}/plugins/kactivitymanagerd/1/kactivitymanagerd_plugin_activitytemplates.so
%attr(755,root,root) %{qt5dir}/plugins/kactivitymanagerd/1/kactivitymanagerd_plugin_eventspy.so
%attr(755,root,root) %{qt5dir}/plugins/kactivitymanagerd/1/kactivitymanagerd_plugin_globalshortcuts.so
%attr(755,root,root) %{qt5dir}/plugins/kactivitymanagerd/1/kactivitymanagerd_plugin_runapplication.so
%attr(755,root,root) %{qt5dir}/plugins/kactivitymanagerd/1/kactivitymanagerd_plugin_slc.so
%attr(755,root,root) %{qt5dir}/plugins/kactivitymanagerd/1/kactivitymanagerd_plugin_sqlite.so
%attr(755,root,root) %{qt5dir}/plugins/kactivitymanagerd/1/kactivitymanagerd_plugin_virtualdesktopswitch.so
%attr(755,root,root) %{qt5dir}/plugins/kcm_activities.so
%attr(755,root,root) %{qt5dir}/plugins/kio_activities.so
%dir %{qt5dir}/qml/org/kde/activities
%{qt5dir}/qml/org/kde/activities/qmldir
%dir %{qt5dir}/qml/org/kde/activities/settings

%attr(755,root,root) %{qt5dir}/qml/org/kde/activities/settings/libkactivitiessettingsplugin.so
%{qt5dir}/qml/org/kde/activities/settings/qmldir
%attr(755,root,root) %{qt5dir}/qml/org/kde/activities/libkactivitiesextensionplugin.so
%dir %{_datadir}/kf5/kactivitymanagerd
%dir %{_datadir}/kf5/kactivitymanagerd/workspace
%dir %{_datadir}/kf5/kactivitymanagerd/workspace/settings
%dir %{_datadir}/kf5/kactivitymanagerd/workspace/settings/qml
%dir %{_datadir}/kf5/kactivitymanagerd/workspace/settings/qml/activitiesTab
%dir %{_datadir}/kf5/kactivitymanagerd/workspace/settings/qml/activityDialog
%dir %{_datadir}/kf5/kactivitymanagerd/workspace/settings/qml/activityDialog/components
%dir %{_datadir}/kf5/kactivitymanagerd/workspace/settings/qml/privacyTab
%{_datadir}/kf5/kactivitymanagerd/workspace/settings/qml/activitiesTab/ActivitiesView.qml
%{_datadir}/kf5/kactivitymanagerd/workspace/settings/qml/activitiesTab/main.qml
%{_datadir}/kf5/kactivitymanagerd/workspace/settings/qml/activityDialog/GeneralTab.qml
%{_datadir}/kf5/kactivitymanagerd/workspace/settings/qml/activityDialog/OtherTab.qml
%{_datadir}/kf5/kactivitymanagerd/workspace/settings/qml/activityDialog/components/DialogButtons.qml
%{_datadir}/kf5/kactivitymanagerd/workspace/settings/qml/activityDialog/components/IconChooser.qml
%{_datadir}/kf5/kactivitymanagerd/workspace/settings/qml/activityDialog/components/LabeledTextField.qml
%{_datadir}/kf5/kactivitymanagerd/workspace/settings/qml/activityDialog/components/ShortcutChooser.qml
%{_datadir}/kf5/kactivitymanagerd/workspace/settings/qml/privacyTab/BlacklistApplicationView.qml

#%%{_datadir}/kf5/kactivitymanagerd/workspace/settings/BlacklistApplicationView.qml
%{_datadir}/kservices5/activities.protocol
%{_datadir}/kservices5/kactivitymanagerd.desktop
%{_datadir}/kservices5/kactivitymanagerd_fileitem_linking_plugin.desktop
#%{_datadir}/kservices5/kactivitymanagerd-plugin-activitytemplates.desktop
#%{_datadir}/kservices5/kactivitymanagerd-plugin-eventspy.desktop
#%{_datadir}/kservices5/kactivitymanagerd-plugin-globalshortcuts.desktop
#%{_datadir}/kservices5/kactivitymanagerd-plugin-slc.desktop
#%{_datadir}/kservices5/kactivitymanagerd-plugin-sqlite.desktop
#%{_datadir}/kservices5/kactivitymanagerd-plugin-virtualdesktopswitch.desktop
%{_datadir}/kservices5/kcm_activities.desktop
%{_datadir}/kservicetypes5/kactivitymanagerd-plugin.desktop

%files devel
%defattr(644,root,root,755)
%{_includedir}/KF5/KActivities
%{_includedir}/KF5/kactivities_version.h
%{_libdir}/cmake/KF5Activities
%attr(755,root,root) %{_libdir}/libKF5Activities.so
%{_pkgconfigdir}/libKActivities.pc
%{qt5dir}/mkspecs/modules/qt_KActivities.pri
