%define _default_patch_fuzz 1
%define _disable_exceptions 1

%bcond_without postgres
%bcond_without mysql
%bcond_without odbc
%bcond_without sqlite
%bcond_without tds
%bcond_without cups
%bcond_without qvfb

%bcond_with docs
%bcond_with debug
%bcond_with ibase
%bcond_with local_phonon_package

#git clone git://gitorious.org/+kde-developers/qt/kde-qt.git
#cd kde-qt
#git archive --format=tar --prefix=kde-qt-everywhere-opensource-src-4.6.2/ master | bzip2 >/tmp/kde-qt-everywhere-opensource-src-4.6.2.tar.bz2
%define with_kde_qt 1
%define kdeqttarballdir kde-qt-everywhere-opensource-src-%{qtversion} 
%define with_qt_snapshot 0

%define qtmajor 4
%define qtminor 7
%define qtsubminor 0

%define qtversion %{qtmajor}.%{qtminor}.%{qtsubminor}

%define libqt %mklibname qt %qtmajor
%define libqtdevel %mklibname qt %qtmajor -d
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
%define libqtmultimedia %mklibname qtmultimedia %qtmajor
%define libphonon %mklibname phonon %qtmajor
%define libqtdeclarative %mklibname qtdeclarative %qtmajor
%define qtlib qt4
%define qtdir %_prefix/lib/qt4
%define pluginsdir %_libdir/qt4/plugins
%define translationdir %qtdir/translations

%if %with_kde_qt
%define qttarballdir kde-qt-everywhere-opensource-src-%{qtversion}
%else
%define qttarballdir qt-everywhere-opensource-src-%{qtversion}
%endif
Name: %{qtlib}
Version: %{qtversion}
Release: %mkrel 0.1
Epoch: 4
Summary: Qt GUI toolkit
Group: Development/KDE and Qt
License: LGPLv2 with exceptions or GPLv3 with exceptions
URL:     http://qt.nokia.com/
%if %with_kde_qt
Source0: http://get.qt.nokia.com/qt/source/%{kdeqttarballdir}.tar.bz2
Source6: qt-everywhere-opensource-src-doc-4.6.2.tar.bz2
%else
Source0: http://get.qt.nokia.com/qt/source/%{qttarballdir}.tar.gz
%endif
Source2: qt4.macros
Source3: mandriva-designer-qt4.desktop 
Source4: mandriva-assistant-qt4.desktop 
Source5: mandriva-linguist-qt4.desktop
Patch0:  qt-x11-opensource-src-4.6.0-qvfb.patch
Patch2:  qt-everywhere-opensource-src-4.6.1-qdoc3.patch
Patch3:  qt-everywhere-opensource-src-4.6.0-fix-str-fmt.patch
Patch4:  qt-everywhere-opensource-src-4.6.1-add_missing_bold_style.diff
Patch5:  qt-everywhere-opensource-src-4.6.1-use_ft_glyph_embolden_to_fake_bold.diff
#(nl): https://bugs.kde.org/180051
Patch6:  qt-everywhere-opensource-src-4.6.1-improve-cups-support.patch
Patch7:  qt-everywhere-opensource-src-gitc0887695-fix-QGraphicsView-crash.patch
Patch8:  qt-everywhere-opensource-src-4.6.2-cups-QTBUG-6471.patch
BuildRequires: libxtst-devel
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
%if %with docs
%dir %{qtdir}/translations
%{qtdir}/translations/qt_*
%endif
%if %{with_kde_qt}
#%_docdir/%name/README.kde-qt
%endif

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

%package -n %{libqtmultimedia}
Summary: QT multimedia lib
Group: System/Libraries
Requires(pre): %{name}-common = %epoch:%version

%description -n %{libqtmultimedia}
QT multimedia lib.

%files -n %{libqtmultimedia}
%defattr(-,root,root,-)
%_libdir/libQtMultimedia.so.%{qtmajor}*

#-------------------------------------------------------------------------

%if %with local_phonon_package

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

%package -n %{libqtdeclarative}
Summary: QT phonon library
Group: System/Libraries
Requires(pre): %{name}-common = %epoch:%version

%description -n %{libqtdeclarative}
Qt phonon library.

%files -n %{libqtdeclarative}
%defattr(-,root,root,-)
%_libdir/libQtDeclarative.so.%{qtmajor}*

#-------------------------------------------------------------------------

%package qmlviewer
Summary: Qt4 qmlviewer utility
Group: Development/KDE and Qt

%description qmlviewer
Qt4 qmlviewer utility.

%files qmlviewer
%defattr(-,root,root,-)
%{qtdir}/bin/qmlviewer
%_libdir/qt4/imports/Qt
%pluginsdir/bearer/libqgenericbearer.so
%pluginsdir/bearer/libqnmbearer.so
%pluginsdir/designer/libqdeclarativeview.so

#-------------------------------------------------------------------------

%package -n %{libqtdevel}
Summary:   Development files for the Qt GUI toolkit
Group:     Development/KDE and Qt
Requires:  %{name}-common = %epoch:%version
Requires:  qt4-qtconfig
Provides:  qt4-devel = %epoch:%version-%release
Provides:  libqt4-devel = %epoch:%version-%release
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
Requires:  %{libqtdeclarative} = %epoch:%version
Requires:  %{libqt3support} = %epoch:%version
Requires:  %{libqt3support} = %epoch:%version
Requires:  %{libqtcore} = %epoch:%version
Requires:  %{libqtdesigner} = %epoch:%version
Requires:  %{libqtgui} = %epoch:%version
Requires:  %{libqtnetwork} = %epoch:%version
Requires:  %{libqtopengl} = %epoch:%version
Requires:  %{libqtsql} = %epoch:%version
Requires:  %{libqtxml} = %epoch:%version
Requires:  %{libqtscripttools} = %epoch:%version
Requires:  %{libqtxmlpatterns} = %epoch:%version
Requires:  %{libqtsvg} = %epoch:%version
Requires:  %{libqtclucene} = %epoch:%version
Requires:  %{libqttest} = %epoch:%version
Requires:  %{libqdbus} = %epoch:%version
Requires:  %{libqtwebkit} = %epoch:%version
Requires:  %{libqtscript} = %epoch:%version
Requires:  %{libqthelp} = %epoch:%version
Requires:  %{libqtmultimedia} = %epoch:%version
%if %with local_phonon_package
Requires:  %{libphonon} = %epoch:%version
%else
Requires:  phonon-devel
%endif
Requires:  qt4-qtdbus = %epoch:%version
Requires:  qt4-designer-plugin-phonon = %epoch:%version
Requires:  qt4-designer-plugin-webkit = %epoch:%version
Requires:  qt4-designer-plugin-qt3support = %epoch:%version
Requires:  mesaglu-devel 
Requires:  png-devel
Requires:  jpeg-devel
Requires:  make

%description -n %{libqtdevel}
The %{qtlib}-devel package contains the files necessary to develop
applications using the Qt GUI toolkit: the header files, the Qt
meta object compiler, and the static libraries.  See the address
http://qt.nokia.com/ for more information about Qt.

Install %{qtlib}-devel if you want to develop GUI applications using the Qt
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
%{qtdir}/bin/xmlpatternsvalidator
%{qtdir}/bin/qttracereplay
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
%if %with docs
%{qtdir}/translations/qtconfig*
%endif

#-------------------------------------------------------------------------

%if %with docs

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

%endif

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
%if %with docs
%{qtdir}/translations/linguist*
%endif

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
%if %with docs
%{qtdir}/translations/assistant*
%endif

#-------------------------------------------------------------------------

%if ! %without odbc

%package database-plugin-odbc
Summary: Database plugin for ODBC Qt support
Group: Development/KDE and Qt
Obsoletes: qt4-database-plugin-odbc-%_lib
BuildRequires: unixODBC-devel
 
%description database-plugin-odbc
Database plugin for ODBC Qt support.

%files database-plugin-odbc
%defattr(-,root,root,-)
%pluginsdir/sqldrivers/libqsqlodbc*

%endif

#-------------------------------------------------------------------------

%if ! %without mysql

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

%if ! %without sqlite

%package database-plugin-sqlite
Summary: Database plugin for sqlite Qt support
Group: Databases
Obsoletes: qt4-database-plugin-sqlite-%_lib
BuildRequires: sqlite3-devel

%description database-plugin-sqlite
Database plugin for sqlite Qt support.

%files database-plugin-sqlite
%defattr(-,root,root,-)
%pluginsdir/sqldrivers/libqsqlite*
%endif

#-------------------------------------------------------------------------

%if ! %without tds

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

%if %with ibase

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

%if ! %without postgres

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
%if %with docs
%{qtdir}/translations/designer_*
%endif

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

%if ! %without qvfb

%package qvfb
Summary: %{qtlib} embedded virtual terminal
Group: Development/KDE and Qt
Conflicts:  %name-common <= 4.3.3-4

%description qvfb
Qt 4 Embedded Virtual Terminal.

%files qvfb
%defattr(-,root,root,-)
%{qtdir}/bin/qvf*
%if %with docs
%{qtdir}/translations/qvfb*
%endif

%endif

#-------------------------------------------------------------------------
#%if %with docs

%package qdoc3
Summary: %{qtlib} documentation generator
Group: Development/KDE and Qt
Conflicts:  %name-common <= 4.3.3-4

%description qdoc3
Qt 4 documentation generator.

%files qdoc3
%defattr(-,root,root,-)
%{qtdir}/bin/qdoc3

#%endif
 
#-------------------------------------------------------------------------

%prep
%if %with_kde_qt 
%setup -n qt 
#-a6
%else
%setup -q -n %{qttarballdir}
%endif

#%patch0 -p0 -b .orig
%if %with docs
%patch2 -p0
%patch3 -p0
%endif
%patch4 -p0
#%patch6 -p0
# REAPPLY ?
##%patch8 -p1

# QMAKE_STRIP need to be clear to allow mdv -debug package
sed -e "s|^QMAKE_STRIP.*=.*|QMAKE_STRIP             =|" -i mkspecs/common/linux.conf
sed -e "s|^QMAKE_CFLAGS_RELEASE.*$|QMAKE_CFLAGS_RELEASE    += %{optflags}|" \
    -e "s|^QMAKE_LFLAGS	.*$|QMAKE_LFLAGS		+= %{ldflags}|" -i mkspecs/common/g++.conf

# let makefile create missing .qm files, the .qm files should be included in qt upstream
for f in translations/*.ts ; do
  touch ${f%.ts}.qm
done

%build
export QTDIR=`/bin/pwd`
export PATH=$QTDIR/bin:$PATH

# Don't include headers or link with /usr/X11R6/{include,lib}
perl -pi -e 's@/X11R6/@/@' mkspecs/linux-*/qmake.conf mkspecs/common/linux.conf

#--------------------------------------------------------

# Removed options from configure
# lets check if it is still necessary
# -L%_prefix/%_lib crashs current build
#
#-L%_prefix/%_lib \
#
#%if ! %without postgres
#-I%{_includedir}/pgsql \
#-I%{_includedir}/pgsql/server \
#
#%if ! %without mysql
#-I%{_includedir}/mysql \

./configure \
   -prefix %{qtdir} \
   -sysconfdir %_sysconfdir \
   -libdir %_libdir \
   -docdir %_docdir/%name/doc \
   -plugindir %pluginsdir \
   -translationdir %translationdir \
%if %with debug
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
   -qdbus \
   -qvfb \
   -qt-gif \
   -gtkstyle \
   -xmlpatterns \
   -opengl desktop \
   -platform linux-g++ \
%if ! %{with_cups}
   -no-cups \
%endif
%if ! %with local_phonon_package
    -no-phonon-backend \
%endif
%if ! %without postgres
   -plugin-sql-psql \
%endif
%if ! %without mysql
   -plugin-sql-mysql \
%else
   -no-sql-mysql \
%endif
%if %with ibase
   -plugin-sql-ibase \
%else
   -no-sql-ibase \
%endif
%if ! %without sqlite
   -plugin-sql-sqlite \
   -system-sqlite \
   -no-sql-sqlite2 \
%else
   -no-sql-sqlite \
   -no-sql-sqlite2 \
%endif
%if ! %without odbc
   -plugin-sql-odbc \
%else
   -no-sql-odbc \
%endif
%if  %without docs
   -nomake demos \
   -nomake examples
%endif

%make

%if ! %without qvfb
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
    %if %with docs
    install_htmldocs \
    install_qchdocs \
    install_translations \
    %endif
    install_qmake \
    install_mkspecs

%if %{with_kde_qt}
#install -m 0644 README.kde-qt %buildroot%_docdir/%name
%endif

# recreate .qm files
LD_LIBRARY_PATH=`pwd`/lib bin/lrelease translations/*.ts

%if ! %without qvfb
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
%if ! %with local_phonon_package
rm -rf %{buildroot}/%_libdir/libphonon.*
rm -rf %{buildroot}/%{qtdir}/include/phonon
rm -rf %{buildroot}/%{_libdir}/pkgconfig/phonon.pc
rm -rf %{buildroot}/%{_libdir}/qt4/plugins/phonon_backend/libphonon_gstreamer.so
%endif

%clean
rm -rf %buildroot
