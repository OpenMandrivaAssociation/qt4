%define _disable_exceptions 1
%define _default_patch_flags -s -l
%define _default_patch_fuzz 2

%bcond_without postgres
%bcond_without mysql
%bcond_without sqlite
%bcond_without tds
%bcond_without cups
%bcond_without docs
%bcond_without openvg
%bcond_without webkit
%bcond_without qvfb

%bcond_with odbc
%bcond_with debug
%bcond_with ibase
%bcond_with phonon

%define major 4

%define _qt4_datadir		%{_prefix}/lib/qt4
%define _qt4_bindir		%{_qt4_datadir}/bin
%define _qt4_docdir		%{_docdir}/qt4
%define _qt4_libdir		%{_libdir}
%define _qt4_includedir		%{_qt4_datadir}/include
%define _qt4_plugindir		%{_libdir}/qt4/plugins
%define _qt4_demodir		%{_qt4_datadir}/demos
%define _qt4_exampledir		%{_qt4_datadir}/examples
%define _qt4_importdir		%{_qt4_datadir}/imports
%define _qt4_translationdir	%{_qt4_datadir}/translations

%define libqt %mklibname qt %{major}
%define libqtdevel %mklibname qt %{major} -d
%define libqt3support %mklibname qt3support %{major}
%define libqtcore %mklibname qtcore %{major}
%define libqtdesigner %mklibname qtdesigner %{major}
%define libqtgui %mklibname qtgui %{major}
%define libqtnetwork %mklibname qtnetwork %{major}
%define libqtopengl %mklibname qtopengl %{major}
%define libqtsql %mklibname qtsql %{major}
%define libqtxml %mklibname qtxml %{major}
%define libqtscripttools %mklibname qtscripttools %{major}
%define libqtxmlpatterns %mklibname qtxmlpatterns %{major}
%define libqtsvg %mklibname qtsvg %{major}
%define libqttest %mklibname qttest %{major}
%define libqdbus %mklibname qtdbus %{major}
%define libqtscript %mklibname qtscript %{major}
%define libqtclucene %mklibname qtclucene %{major}
%define libqthelp %mklibname qthelp %{major}
%define libqtwebkit %mklibname qtwebkit %{major}
%define libqtmultimedia %mklibname qtmultimedia %{major}
%define libphonon %mklibname phonon %{major}
%define libqtdeclarative %mklibname qtdeclarative %{major}


Name:		qt4
Summary:	Qt GUI toolkit
Group:		Development/KDE and Qt
Version:	4.8.0
Release:	1
Epoch:		4
License:	LGPLv2 with exceptions or GPLv3 with exceptions
URL:		http://qt.nokia.com/
Source0: http://get.qt.nokia.com/qt/source/qt-everywhere-opensource-src-%{version}.tar.gz
Source2: qt4.macros
Source3: mandriva-designer-qt4.desktop 
Source4: mandriva-assistant-qt4.desktop 
Source5: mandriva-linguist-qt4.desktop
Patch0:  qt-x11-opensource-src-4.6.0-qvfb.patch
Patch1:  qt-everywhere-opensource-src-4.7.0-force-gb18030-for-gb2312.patch
Patch2:  qt-everywhere-opensource-src-4.7.2-fix-str-fmt.patch
Patch4:  qt-everywhere-opensource-src-4.6.1-add_missing_bold_style.diff
Patch5:  qt-everywhere-opensource-src-4.6.1-use_ft_glyph_embolden_to_fake_bold.diff
Patch7: qt-everywhere-opensource-src-4.8.0-tp-openssl.patch
Patch9: qt-everywhere-opensource-src-4.8.0-rc1-fix-build-with-glib-2.31.patch
Patch10: 	qt-4.8.0-fix-qvfb-build.patch

BuildRequires: libxtst-devel
BuildRequires: libxslt-devel
BuildRequires: libalsa-devel
BuildRequires: pulseaudio-devel
BuildRequires: GL-devel
BuildRequires: Mesa-common-devel
%if %{with openvg}
BuildRequires:	mesaopenvg-devel
%endif
BuildRequires: zlib-devel 
BuildRequires: openssl-devel
BuildRequires: png-devel 
BuildRequires: jpeg-devel
BuildRequires: mng-devel
BuildRequires: lcms-devel
BuildRequires: cups-devel
BuildRequires: freetype2-devel
BuildRequires: pkgconfig(fontconfig)
BuildRequires: expat-devel
BuildRequires: pkgconfig(dbus-1) >= 0.92
BuildRequires: termcap-devel
BuildRequires: pam-devel
BuildRequires: readline-devel
BuildRequires: perl
BuildRequires: glib2-devel
BuildRequires: libxml2-devel
BuildRequires: binutils >= 2.18 
BuildRequires: libxcursor-devel
BuildRequires: libxrandr-devel
BuildRequires: libxrender-devel
BuildRequires: libxv-devel
%if %{with phonon}
BuildRequires: libgstreamer-devel
BuildRequires: libgstreamer-plugins-base-devel
%endif
%if %{with mysql}
BuildRequires: mysql-devel
%endif
%if %{with odbc}
BuildRequires: unixODBC-devel
%endif
%if %{with sqlite}
BuildRequires: sqlite3-devel
%endif
%if %{with tds}
BuildRequires: freetds-devel
%endif
%if %{with ibase}
BuildRequires: firebird-devel
%endif
%if %{with postgres}
BuildRequires: postgresql-devel
BuildRequires: libpq-devel
%endif

%description
Qt is a GUI software toolkit which simplifies the task of writing and
maintaining GUI (Graphical User Interface) applications for the X
Window System. Qt is written in C++ and is fully object-oriented.

This package contains the shared library needed to run Qt
applications, as well as the README files for Qt.

#------------------------------------------------------------------------

%package common
Group: Development/KDE and Qt
Summary: config, language file for Qt

%description common
This package contains all config file and language file.

%files common
%attr(0755,root,root) %_sysconfdir/profile.d/*
%dir %{_qt4_bindir}
%dir %{_qt4_datadir}
%dir %{_qt4_plugindir}
%{_qt4_datadir}/phrasebooks/
%dir %{_qt4_translationdir}
%{_qt4_translationdir}/qt_*

#------------------------------------------------------------------------
# CORE QT LIBRARIES
#--------------------------------------------------------------------

%package -n %{libqtxml}
Summary:	Qt%{major} component library
Group:		System/Libraries
Requires:	%{name}-common = %{epoch}:%{version}
Provides:	qtxmllib = %{epoch}:%{version}-%{release}

%description -n %{libqtxml}
Qt%{major} component library.

%files -n %{libqtxml}
%{_libdir}/libQtXml.so.%{major}*

#--------------------------------------------------------------------
%package -n %{libqtscripttools}
Summary:	Qt%{major} component library
Group:		System/Libraries
Requires:	%{name}-common = %{epoch}:%{version}
Provides:	qtscripttoolslib = %{epoch}:%{version}-%{release}

%description -n %{libqtscripttools}
Qt%{major} component library.

%files -n %{libqtscripttools}
%{_libdir}/libQtScriptTools.so.%{major}*

#--------------------------------------------------------------------
%package -n %{libqtxmlpatterns}
Summary:	Qt%{major} component library
Group:		System/Libraries
Requires:	%{name}-common = %{epoch}:%{version}

%description -n %{libqtxmlpatterns}
Qt%{major} component library.

%files -n %{libqtxmlpatterns}
%{_libdir}/libQtXmlPatterns.so.%{major}*

#--------------------------------------------------------------------
%package -n %{libqtsql}
Summary:	Qt%{major} component library
Group:		System/Libraries
Requires:	%{name}-common = %{epoch}:%{version}
Provides:	qtsqllib = %{epoch}:%{version}-%{release}

%description -n %{libqtsql}
Qt%{major} component library.

%files -n %{libqtsql}
%{_libdir}/libQtSql.so.%{major}*

#--------------------------------------------------------------------
%package -n %{libqtnetwork}
Summary:	Qt%{major} component library
Group:		System/Libraries
Requires:	%{name}-common = %{epoch}:%{version}
Provides:	qtnetworklib = %{epoch}:%{version}-%{release}

%description -n %{libqtnetwork}
Qt%{major} component library.

%files -n %{libqtnetwork}
%{_libdir}/libQtNetwork.so.%{major}*

#--------------------------------------------------------------------
%package -n %{libqtscript}
Summary:	Qt%{major} component library
Group:		System/Libraries
Requires:	%{name}-common = %{epoch}:%{version}
Provides:	libqtscript = %{epoch}:%{version}-%{release}

%description -n %{libqtscript}
Qt%{major} component library.

%files -n %{libqtscript}
%{_libdir}/libQtScript.so.%{major}*
%{_qt4_plugindir}/script/

#--------------------------------------------------------------------
%package -n %{libqtgui}
Summary:	Qt%{major} component library
Group:		System/Libraries
Requires:	%{name}-common = %{epoch}:%{version}
Provides:	qtguilib = %{epoch}:%{version}-%{release}
Conflicts:	%{libqtcore} <= 2:4.2.2-%mkrel 2

%description -n %{libqtgui}
Qt%{major} component library.

%files -n %{libqtgui}
%{_libdir}/libQtGui.so.%{major}*
%{_qt4_plugindir}/imageformats/
%{_qt4_plugindir}/inputmethods/libqimsw-multi.so*

#--------------------------------------------------------------------
%package -n %{libqtsvg}
Summary:	Qt%{major} component library
Group:		System/Libraries
Requires:	%{name}-common = %{epoch}:%{version}
Provides:	qtsvglib = %{epoch}:%{version}-%{release}

%description -n %{libqtsvg}
Qt%{major} component library.

%files -n %{libqtsvg}
%{_libdir}/libQtSvg.so.%{major}*
%{_qt4_plugindir}/iconengines/

#--------------------------------------------------------------------
%package -n %{libqttest}
Summary:	Qt%{major} component library
Group:		System/Libraries
Requires:	%{name}-common = %{epoch}:%{version}
Provides:	qttestlib = %{epoch}:%{version}-%{release}

%description -n %{libqttest}
Qt%{major} component library.

%files -n %{libqttest}
%{_libdir}/libQtTest.so.%{major}*

#--------------------------------------------------------------------
%package -n %{libqtwebkit}
Summary:	Qt%{major} component library
Group:		System/Libraries
Requires:	%{name}-common = %{epoch}:%{version}
Provides:	qtwebkitlib = %{epoch}:%{version}-%{release}

%description -n %{libqtwebkit}
Qt%{major} component library.

%files -n %{libqtwebkit}
%{_libdir}/libQtWebKit.so.%{major}*

#--------------------------------------------------------------------
%package -n %{libqthelp}
Summary:	Qt%{major} component library
Group:		System/Libraries
Requires:	%{name}-common = %{epoch}:%{version}
Provides:	qthelplib = %{epoch}:%{version}-%{release}

%description -n %{libqthelp}
Qt%{major} component library.

%files -n %{libqthelp}
%{_libdir}/libQtHelp.so.%{major}*

#--------------------------------------------------------------------
%package -n %{libqtclucene}
Summary:	Qt%{major} component library
Group:		System/Libraries
Requires:	%{name}-common = %{epoch}:%{version}
Provides:	qtclucenelib = %{epoch}:%{version}-%{release}

%description -n %{libqtclucene}
Qt%{major} component library.

%files -n %{libqtclucene}
%{_libdir}/libQtCLucene.so.%{major}*

#--------------------------------------------------------------------
%package -n %{libqtcore}
Summary:	Qt%{major} component library
Group:		System/Libraries
Requires:	%{name}-common = %{epoch}:%{version}
Provides:	qtcorelib = %{epoch}:%{version}-%{release}
Conflicts:	%{libqtgui} <= 2:4.2.2-%mkrel 2
Obsoletes:	%{_lib}qtuitools4
Obsoletes:	qt4-codecs-plugin-%_lib

%description -n %{libqtcore}
Qt%{major} component library.

%files -n %{libqtcore}
%{_libdir}/libQtCore.so.%{major}*
%{_qt4_plugindir}/codecs/

#--------------------------------------------------------------------
%package -n %{libqt3support}
Summary:	Qt%{major} component library
Group:		System/Libraries
Requires:	%{name}-common = %{epoch}:%{version}
Provides:	qt3supportlib = %{epoch}:%{version}-%{release}

%description -n %{libqt3support}
Qt%{major} component library.

%files -n %{libqt3support}
%{_libdir}/libQt3Support.so.%{major}*

#--------------------------------------------------------------------
%package -n %{libqtopengl}
Summary:	Qt%{major} component library
Group:		System/Libraries
Requires:	%{name}-common = %{epoch}:%{version}
Provides:	qtopengllib = %{epoch}:%{version}-%{release}

%description -n %{libqtopengl}
Qt%{major} component library.

%files -n %{libqtopengl}
%{_libdir}/libQtOpenGL.so.%{major}*

#--------------------------------------------------------------------
%package -n %{libqtdesigner}
Summary:	Qt%{major} component library
Group:		System/Libraries
Requires:	%{name}-common = %{epoch}:%{version}
Provides:	qtdesignerlib = %{epoch}:%{version}-%{release}
# Had wrong major:
Obsoletes:	%{_lib}qtdesigner1 < 2:4.3.4-4

%description -n %{libqtdesigner}
Qt%{major} component library.

%files -n %{libqtdesigner}
%{_libdir}/libQtDesigner.so.%{major}*
%{_libdir}/libQtDesignerComponents.so.%{major}*

#--------------------------------------------------------------------
%package -n %{libqdbus}
Summary:	Qt%{major} dbus library
Group:		System/Libraries
Requires:	%{name}-common = %{epoch}:%{version}
Provides:	qdbuslib = %{epoch}:%{version}-%{release}

%description -n %{libqdbus}
Qt dbus library.

%files -n %{libqdbus}
%{_libdir}/libQtDBus.so.%{major}*

#--------------------------------------------------------------------
%package -n %{libqtmultimedia}
Summary:	Qt%{major} multimedia library
Group:		System/Libraries
Requires:	%{name}-common = %{epoch}:%{version}

%description -n %{libqtmultimedia}
Qt multimedia library.

%files -n %{libqtmultimedia}
%{_libdir}/libQtMultimedia.so.%{major}*

#--------------------------------------------------------------------
%if %{with phonon}
%package -n %{libphonon}
Summary:	Qt%{major} Phonon Library
Group:		System/Libraries
Requires:	%{name}-common = %{epoch}:%{version}

%description -n %{libphonon}
Phonon library for Qt.

%files -n %{libphonon}
%{_libdir}/libphonon.so.%{major}*

#--------------------------------------------------------------------
%package -n phonon-gstreamer
Summary:	Qt%{major} Phonon Gstreamer Backend
Group:		System/Libraries
Provides:	phonon-backend = %{epoch}:%{version}-%{release}
Requires:	gstreamer0.10-plugins-good
Requires:	gstreamer0.10-pulse
Suggests:	gstreamer0.10-ffmpeg
Suggests:	gstreamer0.10-soup
%if %mdkversion >= 201000
Obsoletes: arts
Obsoletes: arts3
%endif

%description -n phonon-gstreamer
Phonon gstreamer backend fot Qt.

%files -n phonon-gstreamer
%{_qt4_plugindir}/phonon_backend/libphonon_gstreamer.so

#--------------------------------------------------------------------
%package designer-plugin-phonon
Summary:	Qt%{major} Designer Phonon Plugin for Qt
Group:		Development/KDE and Qt

%description designer-plugin-phonon
Designer phonon plugin for Qt support.

%files designer-plugin-phonon
%{_qt4_plugindir}/designer/libphononwidgets.so
%endif

#--------------------------------------------------------------------
%package qtdbus
Summary:	Qt%{major} DBus Binary
Group:		Development/KDE and Qt
Requires:	%{libqdbus} = %{epoch}:%{version}

%description qtdbus
Dbus binary for Qt.

%files qtdbus
%{_qt4_bindir}/qdbus
%{_qt4_bindir}/qdbusviewer

#--------------------------------------------------------------------
%package -n %{libqtdeclarative}
Summary:	Qt%{major} phonon library
Group:		System/Libraries
Requires:	%{name}-common = %{epoch}:%{version}

%description -n %{libqtdeclarative}
Qt phonon library.

%files -n %{libqtdeclarative}
%{_libdir}/libQtDeclarative.so.%{major}*

#--------------------------------------------------------------------
%package qmlviewer
Summary:	Qt%{major} Qmlviewer Utility
Group:		Development/KDE and Qt

%description qmlviewer
Qmlviewer utility for Qt.

%files qmlviewer
%{_qt4_bindir}/qmlviewer
%{_qt4_bindir}/qmlplugindump
%{_qt4_importdir}/Qt/
%{_qt4_importdir}/QtWebKit/libqmlwebkitplugin.so
%{_qt4_importdir}/QtWebKit/qmldir
%{_qt4_plugindir}/bearer/libqgenericbearer.so
%{_qt4_plugindir}/bearer/libqnmbearer.so
%{_qt4_plugindir}/bearer/libqconnmanbearer.so
%{_qt4_plugindir}/designer/libqdeclarativeview.so
%dir %{_qt4_plugindir}/qmltooling/
%{_qt4_plugindir}/qmltooling/libqmldbg_tcp.so
%{_qt4_plugindir}/qmltooling/libqmldbg_inspector.so

#--------------------------------------------------------------------
%package -n %{libqtdevel}
Summary:   Development files for the Qt GUI toolkit
Group:     Development/KDE and Qt
Requires:  %{name}-common = %{epoch}:%{version}
Requires:  qt4-qtconfig = %{epoch}:%{version}
Provides:  qt4-devel = %{epoch}:%{version}-%{release}
Provides:  libqt4-devel = %{epoch}:%{version}-%{release}
Requires:  %{libqtdeclarative} = %{epoch}:%{version}
Requires:  %{libqt3support} = %{epoch}:%{version}
Requires:  %{libqt3support} = %{epoch}:%{version}
Requires:  %{libqtcore} = %{epoch}:%{version}
Requires:  %{libqtdesigner} = %{epoch}:%{version}
Requires:  %{libqtgui} = %{epoch}:%{version}
Requires:  %{libqtnetwork} = %{epoch}:%{version}
Requires:  %{libqtopengl} = %{epoch}:%{version}
Requires:  %{libqtsql} = %{epoch}:%{version}
Requires:  %{libqtxml} = %{epoch}:%{version}
Requires:  %{libqtscripttools} = %{epoch}:%{version}
Requires:  %{libqtxmlpatterns} = %{epoch}:%{version}
Requires:  %{libqtsvg} = %{epoch}:%{version}
Requires:  %{libqtclucene} = %{epoch}:%{version}
Requires:  %{libqttest} = %{epoch}:%{version}
Requires:  %{libqdbus} = %{epoch}:%{version}
Requires:  %{libqtwebkit} = %{epoch}:%{version}
Requires:  %{libqtscript} = %{epoch}:%{version}
Requires:  %{libqthelp} = %{epoch}:%{version}
Requires:  %{libqtmultimedia} = %{epoch}:%{version}
%if %{with phonon}
Requires:  qt4-designer-plugin-phonon = %{epoch}:%{version}
%endif
Requires:  qt4-qtdbus = %{epoch}:%{version}
Requires:  qt4-designer-plugin-webkit = %{epoch}:%{version}
Requires:  qt4-designer-plugin-qt3support = %{epoch}:%{version}
Requires(post):	update-alternatives
Requires(postun):update-alternatives
Conflicts:	qt4-common <= 2:4.3.3
Obsoletes: %{mklibname -d QtWebKit} < %version
Conflicts: %{_lib}qtxml4 < 2:4.3.4-3
Conflicts: %{_lib}qtsql4 < 2:4.3.4-3
Conflicts: %{_lib}qtnetwork4 < 2:4.3.4-3
Conflicts: %{_lib}qtscript4 < 2:4.3.4-3
Conflicts: %{_lib}qtgui4 < 2:4.3.4-3
Conflicts: %{_lib}qtsvg4 < 2:4.3.4-3
Conflicts: %{_lib}qttest4 < 2:4.3.4-3
Conflicts: %{_lib}qtcore4 < 2:4.3.4-3
Conflicts: %{_lib}qt3support4 < 2:4.3.4-3
Conflicts: %{_lib}qtopengl4 < 2:4.3.4-3
Conflicts: %{_lib}qtdesigner1 < 2:4.3.4-3
Conflicts: %{_lib}qtdbus4 < 2:4.3.4-3
Conflicts: %{_lib}qassistant1 < 2:4.3.4-3
Conflicts: %{_lib}qttest4 < 2:4.3.4-3
Conflicts: %{_lib}qtcore4 < 2:4.3.4-3
Conflicts: qt4-linguist < 2:4.4.3-3

%description -n %{libqtdevel}
The %{name}-devel package contains the files necessary to develop
applications using the Qt GUI toolkit: the header files, the Qt
meta object compiler, and the static libraries.  See the address
http://qt.nokia.com/ for more information about Qt.

Install %{name}-devel if you want to develop GUI applications using the Qt
toolkit.

%post -n %{libqtdevel}
update-alternatives --install %{_bindir}/qmake qmake %{_qt4_bindir}/qmake 20

%postun -n %{libqtdevel}
if ! [ -e %qtdir/bin/qmake ]; then
  update-alternatives --remove qmake %{_qt4_bindir}/qmake
fi

%files -n %{libqtdevel}
%{_sysconfdir}/rpm/macros.d/qt4.macros
%{_qt4_bindir}/lrelease
%{_qt4_bindir}/lupdate
%{_qt4_bindir}/moc
%{_qt4_bindir}/pixeltool
%{_qt4_bindir}/qdbusxml2cpp
%{_qt4_bindir}/qdbuscpp2xml
%{_qt4_bindir}/qmake
%{_qt4_bindir}/qt3to4
%{_qt4_bindir}/qttracereplay
%{_qt4_bindir}/rcc
%{_qt4_bindir}/uic*
%{_qt4_bindir}/xmlpatternsvalidator
%{_qt4_includedir}/Qt*/
%{_qt4_datadir}/mkspecs/
%{_qt4_datadir}/q3porting.xml
%{_libdir}/*.so
%{_libdir}/*.a
%{_libdir}/*.prl
%{_libdir}/pkgconfig/Qt*.pc

#--------------------------------------------------------------------
%package xmlpatterns
Summary:	Qt%{major} Xmlpatterns Utility
Group:		Development/KDE and Qt

%description xmlpatterns
Xmlpatterns utility for Qt.

%files xmlpatterns
%{_qt4_bindir}/xmlpatterns

#--------------------------------------------------------------------
%package qtconfig
Summary:	Qt%{major} Configuration Utility
Group:		Development/KDE and Qt
Conflicts:	qt4-common <= 2:4.3.3
Requires(post):	update-alternatives
Requires(postun):update-alternatives

%description qtconfig
Main configuration utility for Qt.

%post qtconfig
update-alternatives --install %{_bindir}/qtconfig qtconfig %{_qt4_bindir}/qtconfig 20

%postun qtconfig
if ! [ -e %qtdir/bin/qtconfig ]; then
  update-alternatives --remove qtconfig %{_qt4_bindir}/qtconfig 
fi

%files qtconfig
%{_qt4_bindir}/qtconf*
%{_qt4_translationdir}/qtconfig*

#--------------------------------------------------------------------
%if %{with docs}
%package doc
Summary:	Qt%{major} HTML Documentation
Group:		Books/Computer books
BuildArch:	noarch

%description doc
HTML documentation for the Qt toolkit. To view the documentation,
please load up the file /usr/lib/%{name}/doc/html/index.html in your
favourite browser.

%post doc
# Remove old qt4 doc directories
find %{_docdir} -maxdepth 1 -type d -name qt-4.\* -exec rm -rf {} \;

%files doc
%{_qt4_docdir}/html/
%{_qt4_docdir}/qch/
%{_qt4_docdir}/src/
%endif

#--------------------------------------------------------------------
%if %{with demos}
%package demos
Summary:	Qt%{major} Demonstration Applications
Group:		Development/KDE and Qt
Obsoletes:	%{name}-demos < 4:4.8.0
%if %{with docs}
Requires:	%{name}-doc = %{epoch}:%{version}
%endif
%if %{with examples}
Suggests:	%{name}-examples = %{epoch}:%{version}
%endif

%description demos
Demonstration applications made with Qt %{version}.

%files demos
%{_qt4_bindir}/qtdemo
%{_qt4_demodir}/
%{_qt4_plugindir}/designer/libarthurplugin.so
%endif

#--------------------------------------------------------------------
%if %{with examples}
%package examples
Summary:	Qt%{major} Examples Programs
Group:		Books/Computer books
Obsoletes:	qt4-tutorial
Obsoletes:	%{name}-examples < 4:4.7.0-3

%description examples
Example programs made with Qt %{version}.

%files examples
%{_qt4_exampledir}/
%{_qt4_plugindir}/designer/libcontainerextension.so
%{_qt4_plugindir}/designer/libcustomwidgetplugin.so
%{_qt4_plugindir}/designer/libtaskmenuextension.so
%{_qt4_plugindir}/designer/libworldtimeclockplugin.so
%endif

#--------------------------------------------------------------------
%package linguist
Summary:	Qt%{major} Linguist Translation Utility
Group:		Books/Computer books
Conflicts:	%name-common <= 4.3.3-4

%description linguist
Qt Linguist provides easy translation of Qt GUIs to different.
languages

%files linguist
%{_qt4_bindir}/linguist
%{_qt4_bindir}/lconvert
%{_datadir}/applications/*linguist*.desktop
%{_qt4_translationdir}/linguist*

#--------------------------------------------------------------------
%package assistant
Summary:	Qt%{major} Assistantion Doc Utility
Group:		Books/Computer books
Requires:	qt4-database-plugin-sqlite = %{epoch}:%{version}
Suggests:	qt4-doc = %{epoch}:%{version}
Conflicts:	%name-common <= 4.3.3-4

%description assistant
Qt Assistant provides a documentation Browser.

%files assistant
%{_qt4_bindir}/assistant*
%{_qt4_bindir}/qcollectiongen*
%{_qt4_bindir}/qhelpconv*
%{_qt4_bindir}/qhelpgen*
%{_datadir}/applications/*assistant*.desktop
%{_qt4_translationdir}/assistant*

#--------------------------------------------------------------------
%if %{with odbc}
%package database-plugin-odbc
Summary:	Qt%{major} Database ODBC Plugin
Group:		Development/KDE and Qt
Obsoletes:	qt4-database-plugin-odbc-%_lib
 
%description database-plugin-odbc
Database plugin for ODBC Qt support.

%files database-plugin-odbc
%{_qt4_plugindir}/sqldrivers/libqsqlodbc.so
%endif

#--------------------------------------------------------------------
%if %{with mysql}
%package database-plugin-mysql
Summary:	Qt%{major} Database MYSQL Plugin
Group:		Development/KDE and Qt
Obsoletes:	qt4-database-plugin-mysql-%_lib

%description database-plugin-mysql
Database plugin for mysql Qt support.

%files database-plugin-mysql
%{_qt4_plugindir}/sqldrivers/libqsqlmysql.so
%endif

#--------------------------------------------------------------------
%if %{with sqlite}
%package database-plugin-sqlite
Summary:	Qt%{major} Database SQLITE Plugin
Group:		Databases
Obsoletes:	qt4-database-plugin-sqlite-%_lib

%description database-plugin-sqlite
Database plugin for sqlite Qt support.

%files database-plugin-sqlite
%{_qt4_plugindir}/sqldrivers/libqsqlite.so
%endif

#--------------------------------------------------------------------
%if %{with tds}
%package database-plugin-tds
Summary:	Q%{major} Database FREETDS Plugin
Group:		Databases
Obsoletes:	qt4-database-plugin-tds-%_lib

%description database-plugin-tds
Database plugin for freetds Qt support.

%files database-plugin-tds
%{_qt4_plugindir}/sqldrivers/libqsqltds.so
%endif

#--------------------------------------------------------------------
%if %{with ibase}
%package database-plugin-ibase
Summary:	Qt%{major} Database Interbase Plugin
Group:		Development/KDE and Qt
Obsoletes:	qt4-database-plugin-ibase-%_lib

%description database-plugin-ibase
Database plugin for interbase Qt support.

%files database-plugin-ibase
%{_qt4_plugindir}/sqldrivers/libqsqlibase.so
%endif

#--------------------------------------------------------------------
%if %{with postgres}
%package database-plugin-pgsql
Summary:	Qt%{major} Database PGSQL Plugin
Group:		Development/KDE and Qt
Obsoletes:	qt4-database-plugin-pgsql-%_lib

%description database-plugin-pgsql
Database plugin for pgsql Qt support.

%files database-plugin-pgsql
%{_qt4_plugindir}/sqldrivers/libqsqlpsql.so
%endif

#--------------------------------------------------------------------
%package graphicssystems-plugin
Summary:	Qt%{major} Graphicssystems Plugin
Group:		Development/KDE and Qt
Obsoletes:	qt4-graphicssystems-plugin-%_lib

%description graphicssystems-plugin
Graphicssystems plugins for Qt4.

%files graphicssystems-plugin
%dir %{_qt4_plugindir}/graphicssystems/
%{_qt4_plugindir}/graphicssystems/libqglgraphicssystem.so
%{_qt4_plugindir}/graphicssystems/libqtracegraphicssystem.so
%{_qt4_plugindir}/graphicssystems/libqvggraphicssystem.so

#--------------------------------------------------------------------
%package accessibility-plugin
Summary:	Qt%{major} Accessibility Plugin
Group:		Development/KDE and Qt
Obsoletes:	qt4-accessibility-plugin-%_lib

%description accessibility-plugin
Acessibility plugins for Qt4.

%files accessibility-plugin
%{_qt4_plugindir}/accessible/

#--------------------------------------------------------------------
%package designer
Summary:	Qt%{major} Visual Design Tool
Group:		Development/KDE and Qt
Requires:	%{libqtdevel} = %{epoch}:%{version}
Conflicts:	%name-common <= 4.3.3-4

%description designer
The Qt Designer is a visual design tool that makes designing and
implementing user interfaces a lot easier.

%files designer
%{_qt4_bindir}/design*
%{_datadir}/applications/*designer*.desktop
%{_qt4_translationdir}/designer_*

#--------------------------------------------------------------------
%if %{with webkit}
%package designer-plugin-webkit
Summary:	Qt%{major} Designer Webkit Plugin
Group:		Development/KDE and Qt

%description designer-plugin-webkit
Designer plugin for webkit Qt support.

%files designer-plugin-webkit
%{_qt4_plugindir}/designer/libqwebview.so
%endif

#--------------------------------------------------------------------
%package designer-plugin-qt3support
Summary:	Qt%{major} designer qt3support plugin
Group:		Development/KDE and Qt

%description designer-plugin-qt3support
Designer plugin for qt3support Qt support.

%files designer-plugin-qt3support
%{_qt4_plugindir}/designer/libqt3supportwidgets.so

#--------------------------------------------------------------------
%if %{with qvfb}
%package qvfb
Summary:	Qt%{major} Embedded Virtual Terminal
Group:		Development/KDE and Qt
Conflicts:	%name-common <= 4.3.3-4

%description qvfb
Embedded virtual terminal for Qt support.

%files qvfb
%dir %{_qt4_bindir}
%{_qt4_bindir}/qvfb
%dir %{_qt4_translationdir}
%{_qt4_translationdir}/qvfb*
%endif

#--------------------------------------------------------------------
%package qdoc3
Summary:	Qt%{major} Documentation Generator
Group:		Development/KDE and Qt
Conflicts:	%name-common <= 4.3.3-4

%description qdoc3
Qt 4 documentation generator.

%files qdoc3
%{_qt4_bindir}/qdoc3

#--------------------------------------------------------------------
%prep
%setup -q -n qt-everywhere-opensource-src-%{version}

%patch2 -p1
#%patch4 -p0
%patch7 -p1 -b .ssl
%if %{with webkit}
%patch9 -p1
%endif
%patch10 -p1 -b .fix-qvfb-build

# let makefile create missing .qm files, the .qm files should be included in qt upstream
for f in translations/*.ts ; do
  touch ${f%.ts}.qm
done

# QMAKE_STRIP need to be clear to allow mdv -debug package
sed -e "s|^QMAKE_STRIP.*=.*|QMAKE_STRIP             =|" -i mkspecs/common/linux.conf
sed -e "s|^QMAKE_CFLAGS_RELEASE.*$|QMAKE_CFLAGS_RELEASE    += %{optflags}  -fno-strict-aliasing -DPIC -fPIC| " \
    -e "s|^QMAKE_LFLAGS	.*$|QMAKE_LFLAGS		+= %{ldflags}|" \
    -e "s|^QMAKE_LFLAGS_PLUGIN.*\+= |QMAKE_LFLAGS_PLUGIN += %(echo %ldflags|sed -e 's#-Wl,--no-undefined##') |" \
    -i mkspecs/common/g++.conf

%build
export QTDIR=`/bin/pwd`
export PATH=$QTDIR/bin:$PATH

# Don't include headers or link with /usr/X11R6/{include,lib}
perl -pi -e 's@/X11R6/@/@' mkspecs/linux-*/qmake.conf mkspecs/common/linux.conf

#--------------------------------------------------------

./configure \
   -prefix %{_qt4_datadir} \
   -sysconfdir %{_sysconfdir} \
   -libdir %{_libdir} \
   -docdir %{_qt4_docdir} \
   -plugindir %{_qt4_plugindir} \
   -translationdir %{_qt4_translationdir} \
%if %{with debug}
   -debug \
   -verbose \
%else
   -release \
   -silent \
%endif
   -opensource \
   -confirm-license \
   -shared \
   -no-separate-debug-info \
   -no-rpath \
   -no-pch \
   -optimized-qmake \
   -reduce-relocations \
   -openssl-linked \
   -dbus-linked \
   -gtkstyle \
   -xmlpatterns \
   -opengl desktop \
   -platform linux-g++ \
   -no-gtkstyle \
%if %{with qvfb}
    -qvfb \
%endif
%if !%{with cups}
   -no-cups \
%endif
%if !%{with phonon}
    -no-phonon \
    -no-phonon-backend \
%endif
%if %{with postgres}
    -plugin-sql-psql \
%endif
%if %{with mysql}
    -plugin-sql-mysql \
%else
    -no-sql-mysql \
%endif
%if %{with ibase}
    -plugin-sql-ibase \
%else
    -no-sql-ibase \
%endif
%if %{with sqlite}
    -plugin-sql-sqlite \
    -system-sqlite \
    -no-sql-sqlite2 \
%else
    -no-sql-sqlite \
    -no-sql-sqlite2 \
%endif
%if %{with odbc}
    -plugin-sql-odbc \
%else
    -no-sql-odbc \
%endif
%if %{with tds}
    -plugin-sql-tds \
%else
    -no-sql-tds \
%endif
%if %{with openvg}
    -openvg \
%else
    -no-openvg \
%endif
%if !%{with webkit}
    -no-webkit \
%endif
%if !%{with docs}
    -nomake docs \
%endif
%if !%{with demos}
    -nomake demos \
%endif
%if !%{with examples}
    -nomake examples
%endif

%make

%if %{with qvfb}
    pushd tools/qvfb
    %{_builddir}/qt-everywhere-opensource-src-%{version}/bin/qmake
    %make
    popd
%endif

%install
rm -rf %{buildroot}
install -d %{buildroot}%{_bindir}
install -d %{buildroot}%{_docdir}/%{name}
install -d %{buildroot}%{_sysconfdir}/profile.d

# recreate .qm files
LD_LIBRARY_PATH=`pwd`/lib bin/lrelease translations/*.ts

make install INSTALL_ROOT=%{buildroot}

%if %{with qvfb}
# Install qvfb
%makeinstall -C tools/qvfb INSTALL_ROOT=%{buildroot}
%else
# Remove qvfb translation files that are installed by default
rm -f %{buildroot}%{_qt4_translationdir}/qvfb_*.qm
%endif

%if !%{with docs}
# Remove these doc src files that are installed even if using -nomake-docs
rm -f %{buildroot}%{_qt4_docdir}/src/
%endif

mkdir -p %{buildroot}%{_datadir}/applications
install -m 644 %{SOURCE3} %{buildroot}%{_datadir}/applications
install -m 644 %{SOURCE4} %{buildroot}%{_datadir}/applications
install -m 644 %{SOURCE5} %{buildroot}%{_datadir}/applications

# Fix mkspec link
pushd  %{buildroot}%{_qt4_datadir}/mkspecs
rm -f default
ln -sf %{_qt4_datadir}/mkspecs/linux-g++ default
popd

# Copy examples/tutorial and demos
for subdir in examples demos; do
   for dir in `find $subdir -type d -name .obj`; do rm -rf $dir; done
   for dir in `find $subdir -type d -name .moc`; do rm -rf $dir; done
   cp -a $subdir %{buildroot}/%{_qt4_datadir}
done

# Fix all buildroot paths
find %{buildroot}%{_libdir} -type f -name '*prl' -exec perl -pi -e "s, -L%{_builddir}/\S+,,g" {} \;
find %{buildroot}%{_libdir} -type f -name '*prl' -exec sed -i -e "/^QMAKE_PRL_BUILD_DIR/d" {} \;
find %{buildroot}%{_libdir} -type f -name '*la' -print -exec sed -i -e "s, -L%{_builddir}/?\S+,,g" -e "s,-L../JavaScriptCore/release,,g" -e "s,-ljscore,,g" {} \;
find %{buildroot}/%{_qt4_datadir}/mkspecs -name 'qmake.conf' -exec chmod -x -- {} \;
find %{buildroot}/%{_qt4_datadir}/mkspecs -name Info.plist.app -exec chmod -x -- {} \;

# Don't reference %{builddir} neither /usr(/X11R6)?/ in .pc files.
perl -pi -e '\
s@-L/usr/X11R6/%{_lib} @@g;\
s@-I/usr/X11R6/include @@g;\
s@-L/%{_builddir}\S+@@g'\
    `find . -name \*.pc`

# Install rpm macros
mkdir -p %{buildroot}%{_sysconfdir}/rpm/macros.d
install -m 0644 %{SOURCE2} %{buildroot}%{_sysconfdir}/rpm/macros.d

# Profiles
cat > %{buildroot}%{_sysconfdir}/profile.d/60qt4.sh << EOF
#!/bin/bash

# Qt4 is the main Qt on system
export QTDIR=%{_qt4_datadir}

[ -z \$QT4DOCDIR ] && export QT4DOCDIR=%{_qt4_docdir}

if [ -z \$(echo \$PATH | grep "%{_qt4_bindir}") ]; then
    PATH=\${PATH}:%{_qt4_bindir}
    export PATH
fi

EOF

# Clean WEBKIT test files
rm -fr %{buildroot}%{_qt4_datadir}/tests/qt4/tst_*/

# cleanup
rm -f %{buildroot}%{_libdir}/*.la

