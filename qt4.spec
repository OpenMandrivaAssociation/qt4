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

%define with_debug 0
%{?_with_debug: %{expand: %%global with_debug 1}}

%define enable_static 0
%{?_with_static: %{expand: %%global enable_static 1}}

%define with_cups 1
%{?_without_cups %{expand: %%global with_cups 0}}

%define libqt %mklibname qt %qtmajor
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

%define qtmajor 4
%define qtminor 5
%define qtsubminor 0

%define qtversion %{qtmajor}.%{qtminor}.%{qtsubminor}

%define qtlib qt4
%define qtdir %_prefix/lib/qt4
%define pluginsdir %_libdir/qt4/plugins

%define qttarballdir qt-x11-opensource-src-%{qtversion}

%define date rc1

Name: %{qtlib}
Version: %{qtversion}
Release: %mkrel 0.rc1.9
Epoch: 3
Summary: Qt GUI toolkit
Group: Development/KDE and Qt
License: LGPL
URL:     http://www.qtsoftware.com
Source0: ftp://ftp.trolltech.com/qt/source/%{qttarballdir}-%date.tar.bz2
Source2: qt4.macros
Source3: mandriva-designer-qt4.desktop 
Source4: mandriva-assistant-qt4.desktop 
Source5: mandriva-linguist-qt4.desktop
Source6: Trolltech.conf
Patch0: qt-x11-opensource-src-4.5.0-rc1-valgrind-fix.patch
Patch1: qt-x11-opensource-src-4.5.0-rc1-odbc.patch
# Qt copy patches as usual
Patch195:  0195-compositing-properties.diff
Patch216:  0216-allow-isystem-for-headers.diff
Patch225:  0225-invalidate-tabbar-geometry-on-refresh.patch
Patch245:  0245-fix-randr-changes-detecting.diff
Patch253:  0253-qmake_correct_path_separators.diff
Patch255:  0255-qtreeview-selection-columns-hidden.diff
Patch256:  0272-qiconvcodec-fix.diff
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
%attr(0644,root,root) %_sysconfdir/Trolltech.conf
%dir %{qtdir}
%dir %{qtdir}/bin
%dir %pluginsdir
%{qtdir}/phrasebooks
%dir %{qtdir}/translations
%{qtdir}/translations/qt_*
%_docdir/%name/README

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
%pluginsdir/designer/libqwebview.*

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
%pluginsdir/designer/libqt3supportwidgets.so*

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
Summary(pt_BR): Biblioteca do dbus
Group: System/Libraries
Requires(pre): %{name}-common = %epoch:%version
Requires: %{name}-qtdbus = %epoch:%version
Provides: qdbuslib = %epoch:%version
Conflicts: qt4-devel < 2:4.3.0 

%description -n %{libqdbus}
QT dbus lib.

%files -n %{libqdbus}
%defattr(-,root,root,-)
%_libdir/libQtDBus.so.%{qtmajor}*

#-------------------------------------------------------------------------

%package qtdbus
Summary: QT dbus binary
Summary(pt_BR): Biblioteca do dbus
Group: Development/KDE and Qt

%description qtdbus
QT dbus binary.

%files qtdbus
%defattr(-,root,root,-)
%{qtdir}/bin/qdbus*

#-------------------------------------------------------------------------

%package -n %{libqassistant}
Summary: QT assistant lib
Summary(pt_BR): Biblioteca do qt-assistant
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

%package -n %{libqt}-devel
Summary: Development files for the Qt GUI toolkit
Group: Development/KDE and Qt
Requires: %{name}-common = %epoch:%version
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
Requires: %{libqassistant} = %epoch:%version-%release
Requires: %{libqt3support} = %epoch:%version-%release
Requires: %{libqtcore} = %epoch:%version-%release
Requires: %{libqtdesigner} = %epoch:%version-%release
Requires: %{libqtgui} = %epoch:%version-%release
Requires: %{libqtnetwork} = %epoch:%version-%release
Requires: %{libqtopengl} = %epoch:%version-%release
Requires: %{libqtsql} = %epoch:%version-%release
Requires: %{libqtxml} = %epoch:%version-%release
Requires: %{libqtscripttools} = %epoch:%version-%release
Requires: %{libqtxmlpatterns} = %epoch:%version-%release
Requires: %{libqtsvg} = %epoch:%version-%release
Requires: %{libqtclucene} = %epoch:%version-%release
Requires: %{libqttest} = %epoch:%version-%release
Requires: %{libqdbus} = %epoch:%version-%release
Requires: %{libqtwebkit} = %epoch:%version-%release
Requires: %{libqtscript} = %epoch:%version-%release
Requires: %{libqthelp} = %epoch:%version-%release
Requires: phonon-devel >= 1:4.3.0
Requires: mesaglu-devel 
%description -n %{libqt}-devel
The %{qtlib}-devel package contains the files necessary to develop
applications using the Qt GUI toolkit: the header files, the Qt
meta object compiler, and the static libraries.  See the address
http://www.trolltech.com/products/qt.html for more information
about Qt.
Install qt-devel if you want to develop GUI applications using the Qt
toolkit.

%post -n %{libqt}-devel
update-alternatives --install %_bindir/qmake qmake %qtdir/bin/qmake 20

%postun -n %{libqt}-devel
if ! [ -e %qtdir/bin/qmake ]; then
  update-alternatives --remove qmake %qtdir/bin/qmake
fi

%files -n %{libqt}-devel
%defattr(-,root,root,-)
%{qtdir}/bin/moc*
%{qtdir}/bin/qmake*
%{qtdir}/bin/uic*
%{qtdir}/bin/rcc*
%{qtdir}/bin/qt3to4*
%{qtdir}/bin/pixeltool*
%{qtdir}/bin/lreleas*
%{qtdir}/bin/lupdat*
%_sysconfdir/rpm/macros.d/*
%{qtdir}/include
%{qtdir}/mkspecs
%_libdir/*.so
%_libdir/*.la
%_libdir/*.a
%_libdir/*.prl
%_libdir/pkgconfig/*
%{qtdir}/q3porting.xml
# Phonon header come from Phonon package
%exclude %{qtdir}/include/phonon
%exclude %{qtdir}/include/Qt/phonon*

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
%{qtdir}/translations/qtconfig*

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
%{qtdir}/translations/linguist*

#-------------------------------------------------------------------------

%package assistant
Summary: QT assistantion doc utility
Group: Books/Computer books
Requires: qt4-database-plugin-sqlite
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
%{qtdir}/translations/assistant*

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
Requires: %{libqt}-devel = %epoch:%version
Conflicts:  %name-common <= 4.3.3-4

%description designer
The Qt Designer is a visual design tool that makes designing and
implementing user interfaces a lot easier.

%files designer
%defattr(-,root,root,-)
%{qtdir}/bin/design*
%{_datadir}/applications/*designer*.desktop
%{qtdir}/translations/designer_*

#-------------------------------------------------------------------------

%package qvfb
Summary: %{qtlib} embedded virtual terminal
Group: Development/KDE and Qt
Conflicts:  %name-common <= 4.3.3-4

%description qvfb
Qt 4 Embedded Virtual Terminal.

%files qvfb
%defattr(-,root,root,-)
%{qtdir}/bin/qvf*
%{qtdir}/translations/qvfb*

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
%setup -q -n %{qttarballdir}-%date

%patch0 -p0 -b .valgrind
%patch1 -p0 -b .odbc
%patch195 -p0 -b .qt-copy
%patch216 -p0 -b .qt-copy
%patch225 -p0 -b .qt-copy
%patch245 -p0 -b .qt-copy
%patch253 -p0 -b .qt-copy
%patch255 -p0 -b .qt-copy
%patch256 -p0 -b .qt-copy

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
%else
   -release \
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
   -no-phonon-backend \
   -no-rpath \
   -L%_prefix/%_lib \
   -platform linux-g++ \
   -confirm-license \
   -verbose \
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
        -no-pch \
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

make -C tools/qvfb

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
	install_translations \
	install_mkspecs

install -m 0644 README %buildroot%_docdir/%name

# Install qdoc3
mkdir -p %buildroot/%{qtdir}/tools/qdoc3
install -m 755 tools/qdoc3/qdoc3 %buildroot/%{qtdir}/tools/qdoc3

# Install qvfb
make -C tools/qvfb INSTALL_ROOT=%buildroot install

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

# Phonon needed just in compilation time to enable webkit
rm -f %buildroot/%_libdir/libphonon*
rm -f %buildroot/%pluginsdir/designer/libphonon*
rm -f %buildroot/%_libdir/pkgconfig/phonon*

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

# Conf
cp %SOURCE6 %buildroot%_sysconfdir

%clean
rm -rf %buildroot

