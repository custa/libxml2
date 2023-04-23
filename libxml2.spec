Summary: Library providing XML and HTML support
Name: libxml2
Version: 2.9.12
Release: 16
License: MIT
Group: Development/Libraries
Source: ftp://xmlsoft.org/libxml2/libxml2-%{version}.tar.gz

Patch0: libxml2-multilib.patch
Patch1: Fix-XPath-recursion-limit.patch
Patch2: Fix-Null-deref-in-xmlSchemaGetComponentTargetNs.patch
Patch3: Fix-memleaks-in-xmlXIncludeProcessFlags.patch
Patch4: xmlAddChild-and-xmlAddNextSibling-may-not-attach-the.patch
Patch5: Work-around-lxml-API-abuse.patch
Patch6: Fix-regression-in-xmlNodeDumpOutputInternal.patch
Patch7: Fix-whitespace-when-serializing-empty-HTML-documents.patch
Patch8: Patch-to-forbid-epsilon-reduction-of-final-states.patch
Patch9: Fix-buffering-in-xmlOutputBufferWrite.patch
Patch10:backport-CVE-2022-23308-Use-after-free-of-ID-and-IDREF-attrib.patch
Patch11:backport-CVE-2022-29824-Fix-integer-overflows-in-xmlBuf-and-xmlBuffer.patch
Patch12:Fix-memory-leaks-for-xmlACatalogAdd.patch
Patch13:Fix-memory-leaks-in-xmlACatalogAdd-when-xmlHashAddEntry-failed.patch
Patch14:backport-fix-xmlXPathParserContext-could-be-double-delete-in-.patch
Patch15:backport-Fix-leak-of-xmlElementContent.patch
Patch16:backport-Use-UPDATE_COMPAT-consistently-in-buf.c.patch
Patch17:backport-Prevent-integer-overflow-in-htmlSkipBlankChars-and-x.patch
Patch18:backport-Fix-parsing-of-subtracted-regex-character-classes.patch
Patch19:backport-Restore-behavior-of-htmlDocContentDumpFormatOutput.patch
Patch20:backport-Fix-use-after-free-bugs-when-calling-xmlTextReaderCl.patch
Patch21:backport-Use-xmlNewDocText-in-xmlXIncludeCopyRange.patch
Patch22:backport-xmlBufAvail-should-return-length-without-including-a.patch
Patch23:backport-Fix-integer-overflow-in-xmlBufferDump.patch
Patch24:backport-Fix-missing-NUL-terminators-in-xmlBuf-and-xmlBuffer-.patch
Patch25:backport-Reserve-byte-for-NUL-terminator-and-report-errors-co.patch
Patch26:backport-Fix-unintended-fall-through-in-xmlNodeAddContentLen.patch
Patch27:backport-Don-t-reset-nsDef-when-changing-node-content.patch
Patch28:backport-Avoid-double-free-if-malloc-fails-in-inputPush.patch
Patch29:backport-Fix-memory-leak-in-xmlLoadEntityContent-error-path.patch
Patch30:backport-Reset-nsNr-in-xmlCtxtReset.patch
Patch31:backport-Fix-htmlReadMemory-mixing-up-XML-and-HTML-functions.patch
Patch32:backport-Don-t-initialize-SAX-handler-in-htmlReadMemory.patch
Patch33:backport-Fix-HTML-parser-with-threads-and-without-legacy.patch
Patch34:backport-Fix-xmlCtxtReadDoc-with-encoding.patch
Patch35:backport-Use-xmlStrlen-in-CtxtReadDoc.patch
Patch36:backport-Create-stream-with-buffer-in-xmlNewStringInputStream.patch
Patch37:backport-Use-xmlStrlen-in-xmlNewStringInputStream.patch
Patch38:backport-Fix-memory-leak-with-invalid-XSD.patch
Patch39:backport-Make-XPath-depth-check-work-with-recursive-invocatio.patch
Patch40:backport-CVE-2022-40303-Fix-integer-overflows-with-XML_PARSE_HUGE.patch
Patch41:backport-CVE-2022-40304-Fix-dict-corruption-caused-by-entity-reference-cycles.patch
Patch42:backport-schemas-Fix-null-pointer-deref-in-xmlSchemaCheckCOSS.patch
Patch43:backport-parser-Fix-potential-memory-leak-in-xmlParseAttValue.patch
Patch44:backport-io-Fix-buffer-full-error-with-certain-buffer-sizes.patch
Patch45:backport-io-Check-for-memory-buffer-early-in-xmlParserInputGrow.patch
Patch46:backport-io-Remove-xmlInputReadCallbackNop.patch
Patch47:backport-xmlParseStartTag2-contains-typo-when-checking-for-default.patch
Patch48:backport-parser-Fix-integer-overflow-of-input-ID.patch
Patch49:backport-parser-Don-t-increase-depth-twice-when-parsing-internal.patch
Patch50:backport-CVE-2023-28484-Fix-null-deref-in-xmlSchemaFixupCompl.patch
Patch51:backport-CVE-2023-29469-Hashing-of-empty-dict-strings-isn-t-d.patch

BuildRoot: %{_tmppath}/%{name}-%{version}-root
BuildRequires: python3-devel
BuildRequires: zlib-devel
BuildRequires: pkgconfig
BuildRequires: xz-devel
BuildRequires: libtool
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
Obsoletes: %{name}-static < %{version}-%{release}
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
./autogen.sh
%configure
%make_build

find doc -type f -exec chmod 0644 \{\} \;

%install
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
* Thu Apr 20 2023 BruceGW <gyl93216@163.com> - 2.9.12-16
- Type:CVE
- CVE:CVE-2023-28484 CVE-2023-29469
- SUG:NA
- DESC:fix CVE-2023-28484CVE-2023-29469

* Tue Jan 31 2023 hubin<hubin73@huawei.com> - 2.9.12-15
- Type:bugfix
- CVE:NA
- SUG:NA
- DESC:backport upstream patches

* Mon Nov 21 2022 fuanan <fuanan3@h-partners.com> - 2.9.12-14
- Type:bugfix
- CVE:NA
- SUG:NA
- DESC:backport upstream patches

* Mon Nov 7 2022 Bin Hu <hubin73@huawei.com> - 2.9.12-13
- Type:CVE
- ID:CVE-2022-40303,CVE-2022-40304
- SUG:NA
- DESC:fix CVE-2022-40303,CVE-2022-40304

* Mon Oct 10 2022 chenziyang <chenziyang4@huawei.com> - 2.9.12-12
- Type:bugfix
- ID:NA
- SUG:NA
- DESC:backport patches from upstream

* Tue Sep 13 2022 fuanan <fuanan3@h-partners.com> - 2.9.12-11
- Fix Obsoletes in spec

* Tue Aug 30 2022 fuanan <fuanan3@h-partners.com> - 2.9.12-10
- Type:bugfix
- ID:NA
- SUG:NA
- DESC:backport patches from upstream

* Tue Jul 12 2022 fuanan <fuanan3@h-partners.com> - 2.9.12-9
- Type:bugfix
- ID:NA
- SUG:NA
- DESC:Cleanup duplicate installation

* Fri Jun 24 2022 fuanan <fuanan3@h-partners.com> - 2.9.12-8
- Type:bugfix
- ID:NA
- SUG:NA
- DESC:Fix memory leaks in xmlACatalogAdd when xmlHashAddEntry failed

* Thu Jun 16 2022 fuanan <fuanan3@h-partners.com> - 2.9.12-7
- Type:bugfix
- ID:NA
- SUG:NA
- DESC:Fix memory leaks for xmlACatalogAdd

* Mon May 09 2022 fuanan <fuanan3@h-partners.com> - 2.9.12-6
- Type:CVE
- ID:CVE-2022-29824
- SUG:NA
- DESC:fix CVE-2022-29824

* Wed Mar 09 2022 fuanan <fuanan3@h-partners.com> - 2.9.12-5
- Type:CVE
- ID:CVE-2022-23308
- SUG:NA
- DESC:fix CVE-2022-23308

* Sat Feb 12 2022 fuanan <fuanan3@h-partners.com> - 2.9.12-4
- Type:bugfix
- ID:NA
- SUG:NA
- DESC:use upstream patch refix heap-use-after-free in xmlAddNextSibling and xmlAddChild

* Fri Nov 12 2021 panxiaohe <panxiaohe@huawei.com> - 2.9.12-3
- Type:bugfix
- ID:NA
- SUG:NA
- DESC:add backport bug fixes.
       work around lxml API abuse
       fix regression in xmlNodeDumpOutputInternal
       fix whitespace when serializing empty HTML documents
       forbid epsilon-reduction of final states
       fix buffering in xmlOutputBufferWrite

* Thu Nov 11 2021 panxiaohe <panxiaohe@huawei.com> - 2.9.12-2
- Type:bugfix
- ID:NA
- SUG:NA
- DESC:fix heap-use-after-free in xmlAddNextSibling and xmlAddChild

* Wed Nov 10 2021 Zhipeng Xie <xiezhipeng1@huawei.com> - 2.9.12-1
- Type:enhancement
- ID:NA
- SUG:NA
- DESC:upgrade to upstream v2.9.12

* Tue Nov 9 2021 panxiaohe <panxiaohe@huawei.com> - 2.9.10-19
- Type:bugfix
- ID:NA
- SUG:NA
- DESC:fix memleaks in xmlXIncludeProcessFlags

* Sat Oct 30 2021 huangduirong <huangduirong@huawei.com> - 2.9.10-18
- Type:bugfix
- ID:NA
- SUG:NA
- DESC:fix fuzz issues, fix null-deref in xmlSchemaGetComponentTargetNs

* Sat Oct 23 2021 panxiaohe <panxiaohe@huawei.com> - 2.9.10-17
- Type:bugfix
- ID:NA
- SUG:NA
- DESC:fix fuzz issues
       fix memory leaks in XPointer string-range function
       fix null pointer deref in xmlXPtrRangeInsideFunction
       stop using maxParserDepth in xpath.c
       hardcode maximum XPath recursion depth
       fix XPath recursion limit

* Thu Oct 21 2021 panxiaohe <panxiaohe@huawei.com> - 2.9.10-16
- Type:bugfix
- ID:NA
- SUG:NA
- DESC:fix fuzz issues
       fix heap-use-after-free in xmlXIncludeIncludeNode
       fix stack overflow in xmlDocDumpMemory
       fix stack overflow in htmlDocContentDumpOutput

* Wed Jun 2 2021 guoxiaoqi <guoxiaoqi2@huawei.com> - 2.9.10-15
- Type:CVE
- ID:CVE-2021-3541
- SUG:NA
- DESC:fix CVE-2021-3541

* Sat May 29 2021 zoulin <zoulin13@huawei.com> - 2.9.10-14
- Type:bugfix
- ID:NA
- SUG:NA
- DESC:[add] patches from upstream
       Fix-handling-of-unexpected-EOF-in-xmlParseContent.patch
       Fix-line-numbers-in-error-messages-for-mismatched-ta.patch
       Fix-null-deref-in-legacy-SAX1-parser.patch
       update-for-xsd-language-type-check.patch
       Fix-dangling-pointer-with-xmllint-dropdtd.patch
       Fix-duplicate-xmlStrEqual-calls-in-htmlParseEndTag.patch
       Fix-exponential-behavior-with-recursive-entities.patch
       Fix-quadratic-behavior-when-looking-up-xml-attribute.patch
       Fix-use-after-free-with-xmllint-html-push.patch
       Fix-xmlGetNodePath-with-invalid-node-types.patch
       Stop-checking-attributes-for-UTF-8-validity.patch

* Fri May 28 2021 guoxiaoqi <guoxiaoqi2@huawei.com> - 2.9.10-13
- Type:CVE
- ID:CVE-2021-3517, CVE-2021-3518
- SUG:NA
- DESC:fix CVE-2021-3517 and CVE-2021-3518

* Wed May 26 2021 yangkang <yangkang90@huawei.com> - 2.9.10-12
- Type:CVE
- ID:CVE-2021-3537
- SUG:NA
- DESC:fix CVE-2021-3537

* Tue Mar 2 2021 Lirui <lirui130@huawei.com> - 2.9.10-11
- fix problems detected by oss-fuzz test

* Thu Nov 12 2020 Liquor <lirui130@huawei.com> - 2.9.10-10
- fix problems detected by oss-fuzz test

* Thu Oct 29 2020 panxiaohe <panxiaohe@huawei.com> - 2.9.10-9
- remove subpackage python2-libxml2

* Mon Sep 14 2020 yangzhuangzhuang <yangzhuangzhuang1@huawei.com> - 2.9.10-8
- revert Don-t-try-to-handle-namespaces-when-building-HTML-do.patch.
  rubygem-nokogoro test case fail,because this patch remove xml namespace function.

* Thu Sep 10 2020 yangzhuangzhuang <yangzhuangzhuang1@huawei.com> - 2.9.10-7
- Fixed some issues found in fuzzing testcases

* Fri Aug 28 2020 zoulin <zoulin13@huawei.com> - 2.9.10-6
- Fix more quadratic runtime issues in HTML push parse
- Fix reset HTML parser input before reporting error

* Wed Aug 12 2020 Liquor <lirui130@huawei.com> - 2.9.10-5
- Limit regexp nesting depth
- Fix exponential runtime in xmlFARecurseDeterminism

* Mon Aug 3 2020 Liquor <lirui130@huawei.com> - 2.9.10-4
- Fix integer overflow in xmlFAParseQuantExact

* Tue Jul 28 2020 shenyangyang <shenyangyang4@huawei.com> - 2.9.10-3
- Fix-use-after-free-with-validating-reader and
  Never-expand-parameter-entities-in-text-declaration

* Fri Jul 3 2020 wangchen <wangchen137@huawei.com> - 2.9.10-2
- Sync some patches from community

* Fri Apr 24 2020 BruceGW <gyl93216@163.com> - 2.9.10-1
- update upstream to 2.9.10

* Tue Mar 17 2020 Leo Fang<leofang_94@163.com> - 2.9.8-9
- Sync some patches from community 

* Thu Dec 19 2019 openEuler Buildteam <buildteam@openEuler.org> - 2.9.8-8
- Delete unused infomation

* Tue Sep 24 2019 openEuler Buildteam <buildteam@openeuler.org> - 2.9.8-7
- Fix memory leak in xmlSchemaValidateStream

* Fri Sep 20 2019 openEuler Buildteam <buildteam@openeuler.org> - 2.9.8-6
- Delete redundant information

* Tue Sep 10 2019 openEuler Buildteam <buildteam@openeuler.org> - 2.9.8-5
- Delete epoch

* Thu Sep 5 2019 openEuler Buildteam <buildteam@openeuler.org> - 2.9.8-2
- Backport upstream patches and merge static library to devel package

