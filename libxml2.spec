Summary: Library providing XML and HTML support
Name: libxml2
Version: 2.9.8
Release: 9
License: MIT
Group: Development/Libraries
Source: ftp://xmlsoft.org/libxml2/libxml2-%{version}.tar.gz
Patch0:         libxml2-multilib.patch
# upstream patches
Patch0001:      0001-NaN-and-Inf-fixes-for-pre-C99-compilers.patch
Patch0002:      0002-Revert-Change-calls-to-xmlCharEncInput-to-set-flush-.patch
Patch0003:      0003-Fix-inconsistency-in-xmlXPathIsInf.patch
Patch0004:      0004-Stop-using-XPATH_OP_RESET.patch
Patch0005:      0005-Don-t-change-context-node-in-xmlXPathRoot.patch
Patch0006:      0006-Avoid-unnecessary-backups-of-the-context-node.patch
Patch0007:      0007-Simplify-and-harden-nodeset-filtering.patch
Patch0008:      0008-Improve-restoring-of-context-size-and-position.patch
Patch0009:      0009-HTML-noscript-should-not-close-p.patch
Patch0010:      0010-Remove-a-misleading-line-from-xmlCharEncOutput.patch
Patch0011:      0011-Remove-stray-character-from-comment.patch
Patch0012:      0012-Fix-nullptr-deref-with-XPath-logic-ops.patch
Patch0013:      0013-Fix-infinite-loop-in-LZMA-decompression.patch

Patch6000: Remove-a-misleading-line-from-xmlCharEncOutput.patch
Patch6001: Fix-xmlSchemaValidCtxtPtr-reuse-memory-leak.patch
Patch6002: Reset-HTML-parser-input-pointers-on-encoding-failure.patch
Patch6003: Fix-HTML-serialization-with-UTF-8-encoding.patch
Patch6004: Fix-memory-leak-in-xmlSwitchInputEncodingInt-error-p.patch

Patch6005: Memory-leak-in-xmlFreeID-xmlreader.c.patch
Patch6006: Memory-leak-in-xmlFreeTextReader.patch
Patch6007: Fix-NULL-pointer-deref-in-xmlTextReaderValidateEntit.patch
Patch6008: Fix-commit-Memory-leak-in-xmlFreeID-xmlreader.c.patch
Patch6009: Fix-memory-leaks-in-xmlParseStartTag2-error-paths.patch

Patch6010: 0009-Fix-null-deref-in-xmlregexp-error-path.patch
Patch6011: 0012-Check-XPath-stack-after-calling-functions.patch
Patch6012: 0013-Check-for-integer-overflow-in-xmlXPtrEvalChildSeq.patch
Patch6013: 0021-Fix-memory-leaks-in-xmlXPathParseNameComplex-error-p.patch
Patch6014: 0026-Fix-call-stack-overflow-in-xmlFreePattern.patch
Patch6015: 0031-Fix-parser-termination-from-Double-hyphen-within-com.patch
Patch6016: 0032-Fix-return-value-of-xmlOutputBufferWrite.patch
Patch6017: 0034-Fix-unsigned-integer-overflow.patch
Patch6018: 0037-Fix-memory-leak-in-xmlAllocOutputBufferInternal-erro.patch
Patch6019: backport-Make-xmlParseContent-and-xmlParseElement-non-recursi.patch
Patch6020: backport-Make-xmlFreeNodeList-non-recursive.patch
Patch6021: backport-Make-xmlTextReaderFreeNodeList-non-recursive.patch
Patch6022: backport-Fix-use-after-free-in-xmlTextReaderFreeNodeList.patch
Patch6023: backport-Make-xmlParseConditionalSections-non-recursive.patch
Patch6024: backport-Fix-for-conditional-sections-at-end-of-document.patch
Patch6025: backport-Another-fix-for-conditional-sections-at-end-of-docum.patch
Patch6026: backport-Make-xmlDumpElementContent-non-recursive.patch

Patch9000: Fix-memory-leak-in-xmlParseBalancedChunkMemoryRecove.patch
Patch9001: Fix-memory-leak-in-xmlSchemaValidateStream.patch
Patch6027: backport-fix-infinite-loop-in-xmlStringLenDecodeEntities.patch
Patch6028: backport-Annotate-functions-with-__attribute__-no_sanitize.patch
Patch6029: backport-Avoid-ignored-attribute-warnings-under-GCC.patch

BuildRoot: %{_tmppath}/%{name}-%{version}-root
BuildRequires: python2-devel
BuildRequires: python3-devel
BuildRequires: zlib-devel
BuildRequires: pkgconfig
BuildRequires: xz-devel
URL: http://xmlsoft.org/

%description
This library allows to manipulate XML files. It includes support
to read, modify and write XML and HTML files. There is DTDs support
this includes parsing and validation even with complex DtDs, either
at parse time or later once the document has been modified. The output
can be a simple SAX stream or and in-memory DOM like representations.
In this case one can use the built-in XPath and XPointer implementation
to select sub nodes or ranges. A flexible Input/Output mechanism is
available, with existing HTTP and FTP modules and combined to an
URI library.

%package devel
Summary: Libraries, includes, etc. to develop XML and HTML applications
Group: Development/Libraries
Requires: libxml2 = %{version}-%{release}
Requires: zlib-devel
Requires: xz-devel
Requires: pkgconfig
Obsoletes: %{name}-static
Provides:  %{name}-static

%description devel
Libraries, include files, etc you can use to develop XML applications.
This library allows to manipulate XML files. It includes support
to read, modify and write XML and HTML files. There is DTDs support
this includes parsing and validation even with complex DtDs, either
at parse time or later once the document has been modified. The output
can be a simple SAX stream or and in-memory DOM like representations.
In this case one can use the built-in XPath and XPointer implementation
to select sub nodes or ranges. A flexible Input/Output mechanism is
available, with existing HTTP and FTP modules and combined to an
URI library.

%package -n python2-%{name}
%{?python_provide:%python_provide python-%{name}}
Summary: Python bindings for the libxml2 library
Group: Development/Libraries
Requires: libxml2 = %{version}-%{release}
Obsoletes: %{name}-python < %{version}-%{release}
Provides: %{name}-python = %{version}-%{release}

%description -n python2-%{name}
The libxml2-python package contains a Python 2 module that permits applications
written in the Python programming language, version 2, to use the interface
supplied by the libxml2 library to manipulate XML files.

This library allows to manipulate XML files. It includes support
to read, modify and write XML and HTML files. There is DTDs support
this includes parsing and validation even with complex DTDs, either
at parse time or later once the document has been modified.

%package -n python3-%{name}
Summary: Python 3 bindings for the libxml2 library
Group: Development/Libraries
Requires: libxml2 = %{version}-%{release}
Obsoletes: %{name}-python3 < %{version}-%{release}
Provides: %{name}-python3 = %{version}-%{release}

%description -n python3-%{name}
The libxml2-python3 package contains a Python 3 module that permits
applications written in the Python programming language, version 3, to use the
interface supplied by the libxml2 library to manipulate XML files.

This library allows to manipulate XML files. It includes support
to read, modify and write XML and HTML files. There is DTDs support
this includes parsing and validation even with complex DTDs, either
at parse time or later once the document has been modified.

%package help
Summary:    Man page for libxml2
BuildArch:  noarch

%description  help
%{summary}.


%prep
%autosetup -n %{name}-%{version} -p1

mkdir py3doc
cp doc/*.py py3doc
sed -i 's|#!/usr/bin/python |#!%{__python3} |' py3doc/*.py

%build
%configure
%make_build

find doc -type f -exec chmod 0644 \{\} \;

%install
%make_install

make clean
# for python3
%configure --with-python=%{__python3}
%make_install


rm -f $RPM_BUILD_ROOT%{_libdir}/*.la
rm -f $RPM_BUILD_ROOT%{_libdir}/python*/site-packages/*.a
rm -f $RPM_BUILD_ROOT%{_libdir}/python*/site-packages/*.la
rm -rf $RPM_BUILD_ROOT%{_datadir}/doc/libxml2-%{version}/*
rm -rf $RPM_BUILD_ROOT%{_datadir}/doc/libxml2-python-%{version}/*
(cd doc/examples ; make clean ; rm -rf .deps Makefile)
gzip -9 -c doc/libxml2-api.xml > doc/libxml2-api.xml.gz

%check
make runtests

%clean
rm -fr %{buildroot}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-, root, root)

%doc AUTHORS NEWS README Copyright TODO

%{_libdir}/lib*.so.*
%{_bindir}/xmllint
%{_bindir}/xmlcatalog

%files devel
%defattr(-, root, root)

%doc AUTHORS NEWS README Copyright
%doc doc/*.html doc/html doc/*.gif doc/*.png
%doc doc/tutorial doc/libxml2-api.xml.gz
%doc doc/examples
%doc %dir %{_datadir}/gtk-doc/html/libxml2
%doc %{_datadir}/gtk-doc/html/libxml2/*.devhelp
%doc %{_datadir}/gtk-doc/html/libxml2/*.html
%doc %{_datadir}/gtk-doc/html/libxml2/*.png
%doc %{_datadir}/gtk-doc/html/libxml2/*.css

%{_libdir}/lib*.so
%{_libdir}/*.sh
%{_includedir}/*
%{_bindir}/xml2-config
%{_datadir}/aclocal/libxml.m4
%{_libdir}/pkgconfig/libxml-2.0.pc
%{_libdir}/cmake/libxml2/libxml2-config.cmake

%{_libdir}/*a

%files -n python2-%{name}
%defattr(-, root, root)

%{_libdir}/python2*/site-packages/libxml2.py*
%{_libdir}/python2*/site-packages/drv_libxml2.py*
%{_libdir}/python2*/site-packages/libxml2mod*
%doc python/TODO
%doc python/libxml2class.txt
%doc python/tests/*.py
%doc doc/*.py
%doc doc/python.html

%files -n python3-%{name}
%defattr(-, root, root)

%{_libdir}/python3*/site-packages/libxml2.py*
%{_libdir}/python3*/site-packages/drv_libxml2.py*
%{_libdir}/python3*/site-packages/__pycache__/*py*
%{_libdir}/python3*/site-packages/libxml2mod*
%doc python/TODO
%doc python/libxml2class.txt
%doc py3doc/*.py
%doc doc/python.html

%files help
%doc %{_mandir}/man1/xml2-config.1*
%doc %{_mandir}/man1/xmllint.1*
%doc %{_mandir}/man1/xmlcatalog.1*
%doc %{_mandir}/man3/libxml.3*


%changelog
* Tue Mar 17 2020 Leo Fang<leofang_94@163.com> - 2.9.8-9
- Sync some patches from community 

* Thu Dec 19 2019 openEuler Buildteam <buildteam@openEuler.org> - 2.9.8-8
- Delete unused infomation

* Tue Sep 24 2019 openEuler Buildteam <buildteam@openeuler.org> - 2.9.8-7
- Fix memory leak in xmlSchemaValidateStream

* Fri Sep 20 2019 openEuler Buildteam <buildteam@openeuler.org> - 2.9.8-6
- Delete redundant information

* Thu Sep 10 2019 openEuler Buildteam <buildteam@openeuler.org> - 2.9.8-5
- Delete epoch

* Thu Sep 5 2019 openEuler Buildteam <buildteam@openeuler.org> - 2.9.8-2
- Backport upstream patches and merge static library to devel package

