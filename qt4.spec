%define _default_patch_fuzz 1

%define with_postgres 1
%{?_without_postgres: %{expand: %%global with_postgres 0}}

%define with_mysql 1
%{?_without_mysql: %{expand: %%global with_mysql 0}}

%define with_odbc 1
%{?_without_odbc: %{expand: %%global with_odbc 0}}

%define with_sqlite 1
%{?_without_sqlite: %{expand: %%global with_sqlite 0}}

%define with_ibase 0
%{?_with_ibase: %{expand: %%global with_ibase 1}}

%define with_tds 1
%{?_without_tds: %{expand: %%global with_tds 0}}

%define with_debug 0
%{?_with_debug: %{expand: %%global with_debug 1}}

%define enable_static 0
%{?_with_static: %{expand: %%global enable_static 1}}

%define with_cups 1
%{?_without_cups %{expand: %%global with_cups 0}}

%define with_qvfb 1
%{?_without_qvfb %{expand: %%global with_qvfb 0}}

%define with_kde_qt 1

%define with_local_phonon_package 0

%define qtmajor 4
%define qtminor 5
%define qtsubminor 3

%define qtversion %{qtmajor}.%{qtminor}.%{qtsubminor}

%define libqt %mklibname qt %qtmajor
%define libqtdevel %mklibname qt %qtmajor -d
%define libqassistant %mklibname qassistant %qtmajor
%define libqt3support %mklibname qt3support %qtmajor
%define libqtcore %mklibname qtcore %qtmajor
%define libqtdesigner %mklibname qtdesigner %qtmajor
%define libqtgui %mklibname qtgui %qtmajor
%define libqtnetwork %mklibname qtnetwork %qtmajor
%define libqtopengl %mklibname qtopengl %qtmajor
%define libqtsql %mklibname qtsql %qtmajor
%define libqtxml %mklibname qtxml %qtmajor
%define libqtscripttools %mklibname qtscripttools %qtmajor
%define libqtxmlpatterns %mklibname qtxmlpatterns %qtmajor
%define libqtsvg %mklibname qtsvg %qtmajor
%define libqttest %mklibname qttest %qtmajor
%define libqdbus %mklibname qtdbus %qtmajor
%define libqtscript %mklibname qtscript %qtmajor
%define libqtclucene %mklibname qtclucene %qtmajor
%define libqthelp %mklibname qthelp %qtmajor
%define libqtwebkit %mklibname qtwebkit %qtmajor
%define libphonon %mklibname phonon %qtmajor

%define qtlib qt4
%define qtdir %_prefix/lib/qt4
%define pluginsdir %_libdir/qt4/plugins

%define qttarballdir qt-x11-opensource-src-%{qtversion}

Name: %{qtlib}
Version: %{qtversion}
Release: %mkrel 1
Epoch: 4
Summary: Qt GUI toolkit
Group: Development/KDE and Qt
License: LGPL
URL:     http://www.qtsoftware.com
Source0: ftp://ftp.trolltech.com/qt/source/%{qttarballdir}.tar.gz
Source2: qt4.macros
Source3: mandriva-designer-qt4.desktop 
Source4: mandriva-assistant-qt4.desktop 
Source5: mandriva-linguist-qt4.desktop
# Mandriva patches
Patch0: qt-4.5.2-wformat.patch
# Gitorius patches from kde-qt
# git format-patch v4.5.2..kde-qt/4.5.2-patched
Patch1001: 0001-This-patch-uses-object-name-as-a-fallback-for-window.patch
Patch1002: 0002-This-patch-makes-override-redirect-windows-popup-men.patch
Patch1003: 0003-This-patch-changes-QObjectPrivateVersion-thus-preven.patch
Patch1004: 0004-This-patch-adds-support-for-using-isystem-to-allow-p.patch
Patch1005: 0005-When-tabs-are-inserted-or-removed-in-a-QTabBar.patch
Patch1006: 0006-Fix-configure.exe-to-do-an-out-of-source-build-on-wi.patch
Patch1007: 0007-When-using-qmake-outside-qt-src-tree-it-sometimes-ge.patch
Patch1008: 0008-In-a-treeview-with-columns-like-this.patch
Patch1009: 0009-This-patch-fixes-deserialization-of-values-with-cust.patch
Patch1010: 0010-Import-README.qt-copy-from-the-original-qt-copy.patch
Patch1011: 0011-Update-this-file-to-reflect-the-workflow-with-Git-as.patch
Patch1014: 0014-Add-missing-word-in-sentence.patch
Patch1015: 0015-Building-Qt-documentation-said-to-run-make-install-b.patch
Patch1019: 0019-Make-QMenu-respect-the-minimum-width-set.patch
Patch1020: 0020-Fill-gap-of-X.org-XFree-multimedia-special-launcher-.patch
Patch1021: 0021-Add-support-for-isOpen-in-mysql-driver-plugin.patch
BuildRequires: X11-devel
%if %{enable_static}
BuildRequires: X11-static-devel
%endif
BuildRequires: libxslt-devel
BuildRequires: GL-devel
BuildRequires: Mesa-common-devel
BuildRequires: zlib-devel 
BuildRequires: libpng-devel 
BuildRequires: libjpeg-devel
BuildRequires: libmng-devel
BuildRequires: lcms-devel
BuildRequires: cups-devel
BuildRequires: freetype2-devel
BuildRequires: libfontconfig-devel
BuildRequires: expat-devel
BuildRequires: libdbus-devel >= 0.92
BuildRequires: termcap-devel
BuildRequires: libpam-devel
BuildRequires: readline-devel
BuildRequires: perl
BuildRequires: glib2-devel
BuildRequires: libxml2-devel
BuildRequires: binutils >= 2.18 
# For qtgtk style 
BuildRequires: gtk+2-devel

Provides: %{qtlib}
BuildRoot: %{_tmppath}/%{name}-%{version}-root

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
%defattr(-,root,root,-)
%attr(0755,root,root) %_sysconfdir/profile.d/*
%dir %{qtdir}
%dir %{qtdir}/bin
%dir %pluginsdir
%{qtdir}/phrasebooks
%_docdir/%name/README.kde-qt

#------------------------------------------------------------------------
# CORE QT LIBRARIES
#-------------------------------------------------------------------------

%package -n %{libqtxml}
Summary: QT%{qtmajor} component library
Group: System/Libraries
Requires(pre): %{name}-common = %epoch:%version
Provides:	qtxmllib = %epoch:%version

%description -n %{libqtxml}
QT%{qtmajor} component library.

%files -n %{libqtxml}
%defattr(-,root,root,-)
%_libdir/libQtXml.so.%{qtmajor}*

#-------------------------------------------------------------------------

%package -n %{libqtscripttools}
Summary: QT%{qtmajor} component library
Group: System/Libraries
Requires(pre): %{name}-common = %epoch:%version
Provides: qtscripttoolslib = %epoch:%version

%description -n %{libqtscripttools}
QT%{qtmajor} component library.

%files -n %{libqtscripttools}
%defattr(-,root,root,-)
%_libdir/libQtScriptTools.so.%{qtmajor}*

#-------------------------------------------------------------------------

%package -n %{libqtxmlpatterns}
Summary: QT%{qtmajor} component library
Group: System/Libraries
Requires(pre): %{name}-common = %epoch:%version
Requires: %{name}-xmlpatterns = %epoch:%version

%description -n %{libqtxmlpatterns}
QT%{qtmajor} component library.

%files -n %{libqtxmlpatterns}
%defattr(-,root,root,-)
%_libdir/libQtXmlPatterns.so.%{qtmajor}*

#-------------------------------------------------------------------------

%package -n %{libqtsql}
Summary: QT%{qtmajor} component library
Group: System/Libraries
Requires(pre): %{name}-common = %epoch:%version
Provides:	qtsqllib = %epoch:%version 

%description -n %{libqtsql}
QT%{qtmajor} component library.

%files -n %{libqtsql}
%defattr(-,root,root,-)
%_libdir/libQtSql.so.%{qtmajor}*

#-------------------------------------------------------------------------

%package -n %{libqtnetwork}
Summary: QT%{qtmajor} component library
Group: System/Libraries
Requires(pre): %{name}-common = %epoch:%version
Provides: qtnetworklib = %epoch:%version

%description -n %{libqtnetwork}
QT%{qtmajor} component library.

%files -n %{libqtnetwork}
%defattr(-,root,root,-)
%_libdir/libQtNetwork.so.%{qtmajor}*

#-------------------------------------------------------------------------

%package -n %{libqtscript}
Summary: QT%{qtmajor} component library
Group: System/Libraries
Requires(pre): %{name}-common = %epoch:%version
Provides: libqtscript = %epoch:%version

%description -n %{libqtscript}
QT%{qtmajor} component library.

%files -n %{libqtscript}
%defattr(-,root,root,-)
%_libdir/libQtScript.so.%{qtmajor}*
%pluginsdir/script

#-------------------------------------------------------------------------

%package -n %{libqtgui}
Summary: QT%{qtmajor} component library
Group: System/Libraries
Requires(pre): %{name}-common = %epoch:%version
Conflicts: %{libqtcore} <= 2:4.2.2-%mkrel 2
Provides: qtguilib = %epoch:%version

%description -n %{libqtgui}
QT%{qtmajor} component library.

%files -n %{libqtgui}
%defattr(-,root,root,-)
%_libdir/libQtGui.so.%{qtmajor}*
%pluginsdir/imageformats
%pluginsdir/inputmethods/libqimsw-multi.so*

#-------------------------------------------------------------------------

%package -n %{libqtsvg}
Summary: QT%{qtmajor} component library
Group: System/Libraries
Requires(pre): %{name}-common = %epoch:%version
Provides: qtsvglib = %epoch:%version

%description -n %{libqtsvg}
QT%{qtmajor} component library.

%files -n %{libqtsvg}
%defattr(-,root,root,-)
%_libdir/libQtSvg.so.%{qtmajor}*
%pluginsdir/iconengines/libqsvgicon.*

#-------------------------------------------------------------------------

%package -n %{libqttest}
Summary: QT%{qtmajor} component library
Group: System/Libraries
Requires(pre): %{name}-common = %epoch:%version
Provides: qttestlib = %epoch:%version

%description -n %{libqttest}
QT%{qtmajor} component library.

%files -n %{libqttest}
%defattr(-,root,root,-)
%_libdir/libQtTest.so.%{qtmajor}*

#-------------------------------------------------------------------------

%package -n %{libqtwebkit}
Summary: QT%{qtmajor} component library
Group: System/Libraries
Requires(pre): %{name}-common = %epoch:%version
Provides: qtwebkitlib = %epoch:%version

%description -n %{libqtwebkit}
QT%{qtmajor} component library.

%files -n %{libqtwebkit}
%defattr(-,root,root,-)
%_libdir/libQtWebKit.so.%{qtmajor}*

#-------------------------------------------------------------------------

%package -n %{libqthelp}
Summary: QT%{qtmajor} component library
Group: System/Libraries
Requires(pre): %{name}-common = %epoch:%version
Provides: qthelplib = %epoch:%version

%description -n %{libqthelp}
QT%{qtmajor} component library.

%files -n %{libqthelp}
%defattr(-,root,root,-)
%_libdir/libQtHelp.so.%{qtmajor}*

#-------------------------------------------------------------------------

%package -n %{libqtclucene}
Summary: QT%{qtmajor} component library
Group: System/Libraries
Requires(pre): %{name}-common = %epoch:%version
Provides: qtclucenelib = %epoch:%version

%description -n %{libqtclucene}
QT%{qtmajor} component library.

%files -n %{libqtclucene}
%defattr(-,root,root,-)
%_libdir/libQtCLucene.so.%{qtmajor}*

#-------------------------------------------------------------------------

%package -n %{libqtcore}
Summary: QT%{qtmajor} component library
Group: System/Libraries
Requires(pre): %{name}-common = %epoch:%version
Conflicts: %{libqtgui} <= 2:4.2.2-%mkrel 2
Provides: qtcorelib = %epoch:%version
Obsoletes: %{_lib}qtuitools4
Obsoletes: qt4-codecs-plugin-%_lib

%description -n %{libqtcore}
QT%{qtmajor} component library.

%files -n %{libqtcore}
%defattr(-,root,root,-)
%_libdir/libQtCore.so.%{qtmajor}*
%dir %pluginsdir/codecs
%pluginsdir/codecs/*.so*

#-------------------------------------------------------------------------

%package -n %{libqt3support}
Summary: QT%{qtmajor} component library
Group: System/Libraries
Requires(pre): %{name}-common = %epoch:%version
Provides: qt3supportlib = %epoch:%version

%description -n %{libqt3support}
QT%{qtmajor} component library.

%files -n %{libqt3support}
%defattr(-,root,root,-)
%_libdir/libQt3Support.so.%{qtmajor}*

#-------------------------------------------------------------------------

%package -n %{libqtopengl}
Summary: QT%{qtmajor} component library
Group: System/Libraries
Requires(pre): %{name}-common = %epoch:%version
Provides: qtopengllib = %epoch:%version

%description -n %{libqtopengl}
QT%{qtmajor} component library.

%files -n %{libqtopengl}
%defattr(-,root,root,-)
%_libdir/libQtOpenGL.so.%{qtmajor}*

#-------------------------------------------------------------------------

%package -n %{libqtdesigner}
Summary: QT%{qtmajor} component library
Group: System/Libraries
Requires(pre): %{name}-common = %epoch:%version
Provides: qtdesignerlib = %epoch:%version
# Had wrong major:
Obsoletes: %{_lib}qtdesigner1 < 2:4.3.4-4

%description -n %{libqtdesigner}
QT%{qtmajor} component library.

%files -n %{libqtdesigner}
%defattr(-,root,root,-)
%_libdir/libQtDesigner.so.%{qtmajor}*
%_libdir/libQtDesignerComponents.so.%{qtmajor}*

#-------------------------------------------------------------------------

%package -n %{libqdbus}
Summary: QT dbus lib
Group: System/Libraries
Requires(pre): %{name}-common = %epoch:%version
Provides: qdbuslib = %epoch:%version

%description -n %{libqdbus}
QT dbus lib.

%files -n %{libqdbus}
%defattr(-,root,root,-)
%_libdir/libQtDBus.so.%{qtmajor}*

#-------------------------------------------------------------------------

%if %{with_local_phonon_package}

%package -n %{libphonon}
Summary: QT phonon library
Group: System/Libraries
Requires(pre): %{name}-common = %epoch:%version

%description -n %{libphonon}
Qt phonon library.

%files -n %{libphonon}
%defattr(-,root,root,-)
%_libdir/libphonon.so.%{qtmajor}*

#-------------------------------------------------------------------------

%package -n phonon-gstreamer
Summary: QT phonon gstreamer backend
Group: System/Libraries
Provides: phonon-backend = %{epoch}:%{version}
BuildRequires: libgstreamer-devel
BuildRequires: libgstreamer-plugins-base-devel
Requires: gstreamer0.10-plugins-good
Requires: gstreamer0.10-pulse
Suggests: gstreamer0.10-ffmpeg
Suggests: gstreamer0.10-soup
%if %mdkversion >= 201000
Obsoletes: arts
Obsoletes: arts3
%endif

%description -n phonon-gstreamer
Qt phonon library.

%files -n phonon-gstreamer
%defattr(-,root,root,-)
%pluginsdir/phonon_backend/libphonon_gstreamer.so

%endif

#-------------------------------------------------------------------------

%package qtdbus
Summary: QT dbus binary
Group: Development/KDE and Qt
Requires(pre): %{libqdbus} >= 4:4.5.2

%description qtdbus
QT dbus binary.

%files qtdbus
%defattr(-,root,root,-)
%{qtdir}/bin/qdbus
%{qtdir}/bin/qdbusviewer

#-------------------------------------------------------------------------

%package -n %{libqassistant}
Summary: QT assistant lib
Group: System/Libraries
Requires(pre): %{name}-common = %epoch:%version
Provides: qassistantlib = %epoch:%version
# Had wrong major:
Obsoletes: %{_lib}qassistant1 < 2:4.3.4-4

%description -n %{libqassistant}
QT assistant lib.

%files -n %{libqassistant}
%defattr(-,root,root,-)
%_libdir/libQtAssistantClient.so.%{qtmajor}*

#-------------------------------------------------------------------------

%package -n %{libqtdevel}
Summary: Development files for the Qt GUI toolkit
Group: Development/KDE and Qt
Requires: %{name}-common = %epoch:%version
Requires: qt4-qtconfig
Provides: qt4-devel = %epoch:%version-%release
Provides: libqt4-devel = %epoch:%version-%release
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
Requires: %{libqassistant} = %epoch:%version
Requires: %{libqt3support} = %epoch:%version
Requires: %{libqtcore} = %epoch:%version
Requires: %{libqtdesigner} = %epoch:%version
Requires: %{libqtgui} = %epoch:%version
Requires: %{libqtnetwork} = %epoch:%version
Requires: %{libqtopengl} = %epoch:%version
Requires: %{libqtsql} = %epoch:%version
Requires: %{libqtxml} = %epoch:%version
Requires: %{libqtscripttools} = %epoch:%version
Requires: %{libqtxmlpatterns} = %epoch:%version
Requires: %{libqtsvg} = %epoch:%version
Requires: %{libqtclucene} = %epoch:%version
Requires: %{libqttest} = %epoch:%version
Requires: %{libqdbus} = %epoch:%version
Requires: %{libqtwebkit} = %epoch:%version
Requires: %{libqtscript} = %epoch:%version
Requires: %{libqthelp} = %epoch:%version
%if %{with_local_phonon_package}
Requires: %{libphonon} = %epoch:%version
%else
Requires: phonon-devel
%endif
Requires: qt4-qtdbus = %epoch:%version
Requires: qt4-designer-plugin-phonon = %epoch:%version
Requires: qt4-designer-plugin-webkit = %epoch:%version
Requires: qt4-designer-plugin-qt3support = %epoch:%version
Requires: mesaglu-devel 

%description -n %{libqtdevel}
The %{qtlib}-devel package contains the files necessary to develop
applications using the Qt GUI toolkit: the header files, the Qt
meta object compiler, and the static libraries.  See the address
http://www.trolltech.com/products/qt.html for more information
about Qt.
Install qt-devel if you want to develop GUI applications using the Qt
toolkit.

%post -n %{libqtdevel}
update-alternatives --install %_bindir/qmake qmake %qtdir/bin/qmake 20

%postun -n %{libqtdevel}
if ! [ -e %qtdir/bin/qmake ]; then
  update-alternatives --remove qmake %qtdir/bin/qmake
fi

%files -n %{libqtdevel}
%defattr(-,root,root,-)
%{qtdir}/bin/moc*
%{qtdir}/bin/qmake*
%{qtdir}/bin/uic*
%{qtdir}/bin/rcc*
%{qtdir}/bin/qt3to4*
%{qtdir}/bin/pixeltool*
%{qtdir}/bin/lreleas*
%{qtdir}/bin/lupdat*
%{qtdir}/bin/qdbusxml2cpp
%{qtdir}/bin/qdbuscpp2xml
%_sysconfdir/rpm/macros.d/*
%{qtdir}/include
%{qtdir}/mkspecs
%_libdir/*.so
%_libdir/*.la
%_libdir/*.a
%_libdir/*.prl
%_libdir/pkgconfig/*
%{qtdir}/q3porting.xml

#-------------------------------------------------------------------------

%if %{enable_static}
%package -n %{libqt}-static-devel
Summary: The static library for the Qt GUI toolkit
Group:		Development/KDE and Qt 

%description -n %{libqt}-static-devel
Qt is a GUI software toolkit which simplifies the task of writing and
maintaining GUI (Graphical User Interface) applications for the X
Window System. Qt is written in C++ and is fully object-oriented.

This package contains the shared library needed to run Qt
applications, as well as the README files for Qt.

%files -n %{libqt}-static-devel
%defattr(-,root,root,-)
%_libdir/*.a

%endif

#-------------------------------------------------------------------------

%package xmlpatterns
Summary: Qt4 xmlpatterns utility
Group: Development/KDE and Qt

%description xmlpatterns
Qt4 xmlpatterns utility.

%files xmlpatterns
%defattr(-,root,root,-)
%{qtdir}/bin/xmlpatterns

#-------------------------------------------------------------------------

%package qtconfig
Summary: Main Qt4 configuration utility
Group: Development/KDE and Qt
Conflicts: qt4-common <= 2:4.3.3

%description qtconfig
Main Qt 4.3 configuration utility.

%post qtconfig
update-alternatives --install %_bindir/qtconfig qtconfig %qtdir/bin/qtconfig 20

%postun qtconfig
if ! [ -e %qtdir/bin/qtconfig ]; then
  update-alternatives --remove qtconfig %qtdir/bin/qtconfig 
fi

%files qtconfig
%defattr(-,root,root,-)
%{qtdir}/bin/qtconf*

#-------------------------------------------------------------------------

%package doc
Summary: HTML Documentation for Qt version %{version}
Group: Books/Computer books

%description doc
HTML documentation for the Qt toolkit. To view the documentation,
please load up the file /usr/lib/%{qtlib}/doc/html/index.html in your
favourite browser.

%post doc
# Remove old qt4 doc directories
find %_docdir -maxdepth 1 -type d -name qt-4.\* -exec rm -rf {} \;

%files doc
%defattr(-,root,root,-)
%_docdir/%name/doc/html
%_docdir/%name/doc/qch

#-------------------------------------------------------------------------

%package examples
Summary: Example programs made with Qt version %{version}
Group: Books/Computer books
Obsoletes: qt4-tutorial

%description examples
Example programs made with Qt version %{version}.

%files examples
%defattr(-,root,root,-)
%{qtdir}/examples
%{qtdir}/demos

#-------------------------------------------------------------------------

%package linguist
Summary: QT linguist translation utility
Group: Books/Computer books
Requires(post): desktop-file-utils
Requires(postun): desktop-file-utils
Conflicts:  %name-common <= 4.3.3-4

%description linguist
Qt Linguist provides easy translation of Qt GUIs to different.
languages

%files linguist
%defattr(-,root,root,-)
%{qtdir}/bin/lingu*
%{qtdir}/bin/lconvert*
%{_datadir}/applications/*linguist*.desktop

#-------------------------------------------------------------------------

%package assistant
Summary: QT assistantion doc utility
Group: Books/Computer books
Requires: qt4-database-plugin-sqlite
Suggests: qt4-doc
Requires(post): desktop-file-utils
Requires(postun): desktop-file-utils
Conflicts:  %name-common <= 4.3.3-4

%description assistant
Qt Assistant provides a documentation Browser.

%files assistant
%defattr(-,root,root,-)
%{qtdir}/bin/assistant*
%{qtdir}/bin/qcollectiongen*
%{qtdir}/bin/qhelpconv*
%{qtdir}/bin/qhelpgen*
%{_datadir}/applications/*assistant*.desktop

#-------------------------------------------------------------------------

%if %{with_odbc}

%package database-plugin-odbc
Summary: Database plugin for ODBC Qt support
Group: Development/KDE and Qt
Obsoletes: qt4-database-plugin-odbc-%_lib
BuildRequires: unixODBC-devel
%if %{enable_static}
BuildRequires: unixODBC-static-devel
%endif
 
%description database-plugin-odbc
Database plugin for ODBC Qt support.

%files database-plugin-odbc
%defattr(-,root,root,-)
%pluginsdir/sqldrivers/libqsqlodbc*

%endif

#-------------------------------------------------------------------------

%if %{with_mysql}

%package database-plugin-mysql
Summary: Database plugin for mysql Qt support
Group: Development/KDE and Qt
Obsoletes: qt4-database-plugin-mysql-%_lib
BuildRequires: mysql-devel

%description database-plugin-mysql
Database plugin for mysql Qt support.

%files database-plugin-mysql
%defattr(-,root,root,-)
%pluginsdir/sqldrivers/libqsqlmysql*

%endif

#-------------------------------------------------------------------------

%if %{with_sqlite}

%package database-plugin-sqlite
Summary: Database plugin for sqlite Qt support
Group: Databases
Obsoletes: qt4-database-plugin-sqlite-%_lib
BuildRequires: sqlite3-devel
%if %{enable_static}
BuildRequires: sqlite3-static-devel
%endif

%description database-plugin-sqlite
Database plugin for sqlite Qt support.

%files database-plugin-sqlite
%defattr(-,root,root,-)
%pluginsdir/sqldrivers/libqsqlite*
%endif

#-------------------------------------------------------------------------

%if %{with_tds}

%package database-plugin-tds
Summary: Database plugin for freetds Qt support
Group: Databases
Obsoletes: qt4-database-plugin-tds-%_lib
BuildRequires: freetds-devel

%description database-plugin-tds
Database plugin for freetds Qt support.

%files database-plugin-tds
%defattr(-,root,root,-)
%pluginsdir/sqldrivers/libqsqltds*

%endif

#-------------------------------------------------------------------------

%if %{with_ibase}

%package database-plugin-ibase
Summary: Database plugin for interbase Qt support
Group: Development/KDE and Qt
Obsoletes: qt4-database-plugin-ibase-%_lib
BuildRequires: firebird-devel

%description database-plugin-ibase
Database plugin for interbase Qt support.

%files database-plugin-ibase
%defattr(-,root,root,-)
%pluginsdir/sqldrivers/libqsqlibase*
%endif

#-------------------------------------------------------------------------

%if %{with_postgres}

%package database-plugin-pgsql
Summary: Database plugin for pgsql Qt support
Group: Development/KDE and Qt
Obsoletes: qt4-database-plugin-pgsql-%_lib
BuildRequires: postgresql-devel
BuildRequires: libpq-devel

%description database-plugin-pgsql
Database plugin for pgsql Qt support.

%files database-plugin-pgsql
%defattr(-,root,root,-)
%pluginsdir/sqldrivers/libqsqlpsql*

%endif

#-------------------------------------------------------------------------

%package graphicssystems-plugin
Summary: Graphicssystems plugins for Qt4
Group: Development/KDE and Qt
Obsoletes: qt4-graphicssystems-plugin-%_lib

%description graphicssystems-plugin
Graphicssystems plugins for Qt4.

%files graphicssystems-plugin
%defattr(-,root,root,-)
%dir %pluginsdir/graphicssystems
%pluginsdir/graphicssystems/*

#-------------------------------------------------------------------------

%package accessibility-plugin
Summary: Accessibility plugins for Qt4
Group: Development/KDE and Qt
Obsoletes: qt4-accessibility-plugin-%_lib

%description accessibility-plugin
Acessibility plugins for Qt4.

%files accessibility-plugin
%defattr(-,root,root,-)
%dir %pluginsdir/accessible
%pluginsdir/accessible/*

#-------------------------------------------------------------------------

%package designer
Summary: %{qtlib} visual design tool
Group: Development/KDE and Qt
Requires: %{libqtdevel} = %epoch:%version
Conflicts:  %name-common <= 4.3.3-4

%description designer
The Qt Designer is a visual design tool that makes designing and
implementing user interfaces a lot easier.

%files designer
%defattr(-,root,root,-)
%{qtdir}/bin/design*
%{_datadir}/applications/*designer*.desktop

#-------------------------------------------------------------------------

%package designer-plugin-phonon
Summary: designer plugin for phonon Qt support
Group: Development/KDE and Qt

%description designer-plugin-phonon
designer plugin for phonon Qt support.

%files designer-plugin-phonon
%defattr(-,root,root,-)
%pluginsdir/designer/libphonon*

#-------------------------------------------------------------------------

%package designer-plugin-webkit
Summary: designer plugin for webkit Qt support
Group: Development/KDE and Qt

%description designer-plugin-webkit
designer plugin for webkit Qt support.

%files designer-plugin-webkit
%defattr(-,root,root,-)
%pluginsdir/designer/libqwebview*

#-------------------------------------------------------------------------

%package designer-plugin-qt3support
Summary: designer plugin for qt3support Qt support
Group: Development/KDE and Qt

%description designer-plugin-qt3support
designer plugin for qt3support Qt support.

%files designer-plugin-qt3support
%defattr(-,root,root,-)
%pluginsdir/designer/libqt3supportwidget*

#-------------------------------------------------------------------------

%if %{with_qvfb}

%package qvfb
Summary: %{qtlib} embedded virtual terminal
Group: Development/KDE and Qt
Conflicts:  %name-common <= 4.3.3-4

%description qvfb
Qt 4 Embedded Virtual Terminal.

%files qvfb
%defattr(-,root,root,-)
%{qtdir}/bin/qvf*

%endif

#-------------------------------------------------------------------------

%package qdoc3
Summary: %{qtlib} documentation generator
Group: Development/KDE and Qt
Conflicts:  %name-common <= 4.3.3-4

%description qdoc3
Qt 4 documentation generator.

%files qdoc3
%defattr(-,root,root,-)
%{qtdir}/tools/qdoc3

#-------------------------------------------------------------------------

%prep
%setup -q -n %{qttarballdir}
%patch0 -p0 -b .mandriva
%patch1001 -p1 -b .kde-qt
%patch1002 -p1 -b .kde-qt
%patch1003 -p1 -b .kde-qt
%patch1004 -p1 -b .kde-qt
%patch1005 -p1 -b .kde-qt
%patch1006 -p1 -b .kde-qt
%patch1007 -p1 -b .kde-qt
%patch1008 -p1 -b .kde-qt
%patch1009 -p1 -b .kde-qt
%patch1010 -p1 -b .kde-qt
%patch1011 -p1 -b .kde-qt
%patch1014 -p1 -b .kde-qt
%patch1015 -p1 -b .kde-qt
%patch1019 -p1 -b .kde-qt
%patch1020 -p1 -b .kde-qt
%patch1021 -p1 -b .kde-qt

# QMAKE_STRIP need to be clear to allow mdv -debug package
sed -e "s|^QMAKE_STRIP.*=.*|QMAKE_STRIP             =|" -i mkspecs/common/linux.conf
sed -e "s|^QMAKE_CFLAGS_RELEASE.*$|QMAKE_CFLAGS_RELEASE    += %{optflags}|" \
    -e "s|^QMAKE_LFLAGS	.*$|QMAKE_LFLAGS		+= %{ldflags}|" -i mkspecs/common/g++.conf


%build
export QTDIR=`/bin/pwd`
export PATH=$QTDIR/bin:$PATH

# Don't include headers or link with /usr/X11R6/{include,lib}
perl -pi -e 's@/X11R6/@/@' mkspecs/linux-*/qmake.conf mkspecs/common/linux.conf

#--------------------------------------------------------
# function configure
function qt_configure {

echo "yes" |
./configure \
	-prefix %{qtdir} \
	-qdbus \
%if %{with_debug}
   -debug \
   -verbose \
%else
   -release \
   -silent \
%endif
   -sysconfdir %_sysconfdir \
   -libdir %_libdir \
   -docdir %_docdir/%name/doc \
   -plugindir %pluginsdir \
   -qvfb \
   -qt-gif \
%if ! %{with_cups}
   -no-cups \
%endif
   -no-separate-debug-info \
   -no-rpath \
   -reduce-relocations \
   -opengl desktop \
   -L%_prefix/%_lib \
   -platform linux-g++ \
   -confirm-license \
%if ! %{with_local_phonon_package}
	-no-phonon-backend \
%endif
   -opensource \
	$*
}

# static
%if %{enable_static}
	qt_configure \
   %if %{with_odbc}
   -qt-sql-odbc \
   %endif
   %if %{with_sqlite}
   -qt-sql-sqlite \
   -system-sqlite \
   -no-sql-sqlite2 \
   %else
   -no-sql-sqlite \
   -no-sql-sqlite2 \
   %endif
   -nomake demos \
   -nomake examples \
   -nomake tools \
   -static

   %make

	mkdir safelib
	cp lib/*.a safelib
%endif

# shared
qt_configure -shared \
   %if %{with_postgres}
   -plugin-sql-psql \
   -I%{_includedir}/pgsql \
   -I%{_includedir}/pgsql/server \
   %endif
   %if %{with_mysql}
   -plugin-sql-mysql \
   -I%{_includedir}/mysql \
   %else
   -no-sql-mysql \
   %endif
   %if %{with_ibase}
   -plugin-sql-ibase \
   %else
   -no-sql-ibase \
   %endif
   %if %{with_sqlite}
   -plugin-sql-sqlite \
   -system-sqlite \
   -no-sql-sqlite2 \
   %else
   -no-sql-sqlite \
   -no-sql-sqlite2 \
   %endif
   %if %{with_odbc}
   -plugin-sql-odbc \
   %else
   -no-sql-odbc \
   %endif
   -nomake demos \
   -nomake examples 

%make

%make sub-tools-qdoc3

%if %{with_qvfb}
	make -C tools/qvfb
%endif

%install
rm -rf %buildroot
install -d %buildroot%_bindir
install -d %buildroot%_docdir/%name
install -d %buildroot%_sysconfdir
install -d %buildroot%_sysconfdir/profile.d

make INSTALL_ROOT=%buildroot \
	sub-tools-install_subtargets-ordered \
	install_htmldocs \
	install_qchdocs \
	install_qmake \
	install_mkspecs

install -m 0644 README.kde-qt %buildroot%_docdir/%name

# Install qdoc3
mkdir -p %buildroot/%{qtdir}/tools/qdoc3
install -m 755 tools/qdoc3/qdoc3 %buildroot/%{qtdir}/tools/qdoc3

%if %{with_qvfb}
	# Install qvfb
	%make -C tools/qvfb INSTALL_ROOT=%buildroot install
%endif

mkdir -p %buildroot%_datadir/applications
install -m 644 %SOURCE3 %buildroot%_datadir/applications
install -m 644 %SOURCE4 %buildroot%_datadir/applications
install -m 644 %SOURCE5 %buildroot%_datadir/applications

# Fix mkspec link
pushd  %buildroot%{qtdir}/mkspecs
rm -f default
ln -sf %{qtdir}/mkspecs/linux-g++ default
popd

# Copy examples/tutorial and demos
for subdir in examples demos; do
   for dir in `find $subdir -type d -name .obj`; do rm -rf $dir; done
   for dir in `find $subdir -type d -name .moc`; do rm -rf $dir; done
   cp -a $subdir %buildroot/%{qtdir}
done

%if %{enable_static}
	cp safelib/* %buildroot/%_libdir
%endif

# Fix all buildroot paths
find %buildroot/%_libdir -type f -name '*prl' -exec perl -pi -e "s, -L%_builddir/\S+,,g" {} \;
find %buildroot/%_libdir -type f -name '*prl' -exec sed -i -e "/^QMAKE_PRL_BUILD_DIR/d" {} \;
find %buildroot/%_libdir -type f -name '*la' -print -exec perl -pi -e "s, -L%_builddir/?\S+,,g" {} \;
find %buildroot/%qtdir/mkspecs -name 'qmake.conf' -exec chmod -x -- {} \;
find %buildroot/%qtdir/mkspecs -name Info.plist.app -exec chmod -x -- {} \;

# Don't reference %{builddir} neither /usr(/X11R6)?/ in .pc files.
perl -pi -e '\
s@-L/usr/X11R6/%{_lib} @@g;\
s@-I/usr/X11R6/include @@g;\
s@-L/%{_builddir}\S+@@g'\
    `find . -name \*.pc`

# Install rpm macros
mkdir -p %buildroot/%_sysconfdir/rpm/macros.d
install -m 0644 %SOURCE2 %buildroot/%_sysconfdir/rpm/macros.d

# Profiles
cat > %buildroot%_sysconfdir/profile.d/60qt4.sh << EOF
#!/bin/bash

# Qt4 is the main Qt on system
export QTDIR=%qtdir

[ -z \$QT4DOCDIR ] && export QT4DOCDIR=%_docdir/qt4/doc

if [ -z \$(echo \$PATH | grep "%{qtdir}/bin") ]; then
    PATH=\${PATH}:%{qtdir}/bin
    export PATH
fi

EOF

# We need a proper removal
%if ! %{with_local_phonon_package}
rm -rf %{buildroot}/%_libdir/libphonon.*
rm -rf %{buildroot}/%{qtdir}/include/phonon
rm -rf %{buildroot}/%{_libdir}/pkgconfig/phonon.pc
%endif


%clean
rm -rf %buildroot

