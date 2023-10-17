Summary: Library providing XML and HTML support
Name: libxml2
Version: 2.9.14
Release: 9
License: MIT
Group: Development/Libraries
Source: https://download.gnome.org/sources/%{name}/2.9/%{name}-%{version}.tar.xz

Patch0: libxml2-multilib.patch
Patch1: Fix-memleaks-in-xmlXIncludeProcessFlags.patch
Patch2: Fix-memory-leaks-for-xmlACatalogAdd.patch
Patch3: Fix-memory-leaks-in-xmlACatalogAdd-when-xmlHashAddEntry-failed.patch
Patch4: backport-CVE-2022-40303-Fix-integer-overflows-with-XML_PARSE_.patch
Patch5: backport-CVE-2022-40304-Fix-dict-corruption-caused-by-entity-.patch
Patch6: backport-schemas-Fix-null-pointer-deref-in-xmlSchemaCheckCOSS.patch
Patch7: backport-parser-Fix-potential-memory-leak-in-xmlParseAttValue.patch

Patch6000:  backport-Add-whitespace-folding-for-some-atomic-data-types-th.patch
Patch6001:  backport-Properly-fold-whitespace-around-the-QName-value-when.patch
Patch6002:  backport-Avoid-arithmetic-on-freed-pointers.patch
Patch6003:  backport-fix-xmlXPathParserContext-could-be-double-delete-in-.patch
Patch6004:  backport-Use-UPDATE_COMPAT-consistently-in-buf.c.patch
Patch6005:  backport-Restore-behavior-of-htmlDocContentDumpFormatOutput.patch
Patch6006:  backport-Fix-use-after-free-bugs-when-calling-xmlTextReaderCl.patch
Patch6007:  backport-Use-xmlNewDocText-in-xmlXIncludeCopyRange.patch
Patch6008:  backport-xmlBufAvail-should-return-length-without-including-a.patch
Patch6009:  backport-Fix-integer-overflow-in-xmlBufferDump.patch
Patch6010:  backport-Fix-missing-NUL-terminators-in-xmlBuf-and-xmlBuffer-.patch
Patch6011:  backport-Reserve-byte-for-NUL-terminator-and-report-errors-co.patch
Patch6012:  backport-Fix-unintended-fall-through-in-xmlNodeAddContentLen.patch
Patch6013:  backport-Don-t-reset-nsDef-when-changing-node-content.patch
Patch6014:  backport-Avoid-double-free-if-malloc-fails-in-inputPush.patch
Patch6015:  backport-Fix-memory-leak-in-xmlLoadEntityContent-error-path.patch
Patch6016:  backport-Reset-nsNr-in-xmlCtxtReset.patch
Patch6017:  backport-Fix-htmlReadMemory-mixing-up-XML-and-HTML-functions.patch
Patch6018:  backport-Don-t-initialize-SAX-handler-in-htmlReadMemory.patch
Patch6019:  backport-Fix-HTML-parser-with-threads-and-without-legacy.patch
Patch6020:  backport-Fix-xmlCtxtReadDoc-with-encoding.patch
Patch6021:  backport-Use-xmlStrlen-in-CtxtReadDoc.patch
Patch6022:  backport-Create-stream-with-buffer-in-xmlNewStringInputStream.patch
Patch6023:  backport-Use-xmlStrlen-in-xmlNewStringInputStream.patch
Patch6024:  backport-Fix-memory-leak-with-invalid-XSD.patch
Patch6025:  backport-Make-XPath-depth-check-work-with-recursive-invocatio.patch
Patch6026:  backport-Fix-overflow-check-in-SAX2.c.patch
Patch6027:  backport-xinclude-Fix-memory-leak-when-fuzzing.patch
Patch6028:  backport-xinclude-Fix-more-memory-leaks-in-xmlXIncludeLoadDoc.patch
Patch6029:  backport-schemas-Fix-infinite-loop-in-xmlSchemaCheckElemSubst.patch
Patch6030:  backport-malloc-fail-Fix-memory-leak-in-xmlCreatePushParserCt.patch
Patch6031:  backport-malloc-fail-Fix-memory-leak-in-xmlStaticCopyNodeList.patch
Patch6032:  backport-malloc-fail-Fix-memory-leak-in-xmlNewPropInternal.patch
Patch6033:  backport-malloc-fail-Fix-memory-leak-in-xmlNewDocNodeEatName.patch
Patch6034:  backport-malloc-fail-Fix-infinite-loop-in-xmlSkipBlankChars.patch
Patch6035:  backport-malloc-fail-Fix-memory-leak-in-xmlSAX2ExternalSubset.patch
Patch6036:  backport-malloc-fail-Fix-memory-leak-in-xmlParseReference.patch
Patch6037:  backport-malloc-fail-Fix-use-after-free-in-xmlXIncludeAddNode.patch
Patch6038:  backport-malloc-fail-Fix-memory-leak-in-xmlStringGetNodeList.patch
Patch6039:  backport-parser-Fix-error-message-in-xmlParseCommentComplex.patch
Patch6040:  backport-io-Fix-buffer-full-error-with-certain-buffer-sizes.patch
Patch6041:  backport-reader-Switch-to-xmlParserInputBufferCreateMem.patch
Patch6042:  backport-uri-Allow-port-without-host.patch
Patch6043:  backport-parser-Fix-consumed-accounting-when-switching-encodi.patch
Patch6044:  backport-html-Fix-check-for-end-of-comment-in-push-parser.patch
Patch6045:  backport-parser-Fix-push-parser-with-1-3-byte-initial-chunk.patch

Patch6047:  backport-parser-Restore-parser-state-in-xmlParseCDSect.patch
Patch6048:  backport-parser-Remove-dangerous-check-in-xmlParseCharData.patch
Patch6049:  backport-parser-Don-t-call-DefaultSAXHandlerInit-from-xmlInit.patch
Patch6050:  backport-Correctly-relocate-internal-pointers-after-realloc.patch
Patch6051:  backport-Avoid-creating-an-out-of-bounds-pointer-by-rewriting.patch
Patch6052:  backport-error-Make-sure-that-error-messages-are-valid-UTF-8.patch
Patch6053:  backport-io-Check-for-memory-buffer-early-in-xmlParserInputGrow.patch
Patch6054:  backport-io-Remove-xmlInputReadCallbackNop.patch
Patch6055:  backport-Revert-uri-Allow-port-without-host.patch
Patch6056:  backport-xmlParseStartTag2-contains-typo-when-checking-for-default.patch
Patch6057:  backport-parser-Fix-integer-overflow-of-input-ID.patch
Patch6058:  backport-parser-Don-t-increase-depth-twice-when-parsing-internal.patch
Patch6059:  backport-xpath-number-should-return-NaN.patch
Patch6060:  backport-error-Don-t-move-past-current-position.patch
Patch6061:  backport-malloc-fail-Handle-memory-errors-in-xmlTextReaderEntPush.patch
Patch6062:  backport-malloc-fail-Fix-infinite-loop-in-xmlParseTextDecl.patch
Patch6063:  backport-malloc-fail-Fix-null-deref-in-xmlAddDefAttrs.patch
Patch6064:  backport-malloc-fail-Fix-null-deref-if-growing-input-buffer-fails.patch
Patch6065:  backport-malloc-fail-Fix-null-deref-in-xmlSAX2AttributeInternal.patch
Patch6066:  backport-malloc-fail-Fix-null-deref-in-xmlBufResize.patch
Patch6067:  backport-buf-Fix-return-value-of-xmlBufGetInputBase.patch
Patch6068:  backport-malloc-fail-Don-t-call-xmlErrMemory-in-xmlstring.c.patch
Patch6069:  backport-malloc-fail-Fix-reallocation-in-inputPush.patch
Patch6070:  backport-malloc-fail-Fix-use-after-free-in-xmlParseStartTag2.patch
Patch6071:  backport-malloc-fail-Add-error-checks-in-xmlXPathEqualValuesCommon.patch
Patch6072:  backport-malloc-fail-Add-error-check-in-xmlXPathEqualNodeSetFloat.patch
Patch6073:  backport-malloc-fail-Fix-error-check-in-xmlXPathCompareValues.patch
Patch6074:  backport-malloc-fail-Record-malloc-failure-in-xmlXPathCompLiteral.patch
Patch6075:  backport-malloc-fail-Check-return-value-of-xmlXPathNodeSetDupNs.patch
Patch6076:  backport-malloc-fail-Fix-null-deref-in-xmlXIncludeLoadTxt.patch
Patch6077:  backport-malloc-fail-Fix-reallocation-in-xmlXIncludeNewRef.patch
Patch6078:  backport-xinclude-Fix-quadratic-behavior-in-xmlXIncludeLoadTx.patch
Patch6079:  backport-malloc-fail-Fix-memory-leak-in-xmlParserInputBufferCreateMem.patch
Patch6080:  backport-malloc-fail-Check-for-malloc-failure-in-xmlFindCharEncodingHandler.patch
Patch6081:  backport-malloc-fail-Fix-leak-of-xmlCharEncodingHandler.patch
Patch6082:  backport-malloc-fail-Fix-memory-leak-in-xmlParseEntityDecl.patch
Patch6083:  backport-encoding-Cast-toupper-argument-to-unsigned-char.patch
Patch6084:  backport-malloc-fail-Fix-memory-leak-in-xmlXPathCompareValues.patch
Patch6085:  backport-malloc-fail-Fix-memory-leak-in-xmlXPathTryStreamCompile.patch
Patch6086:  backport-malloc-fail-Fix-memory-leak-after-calling-valuePush.patch
Patch6087:  backport-malloc-fail-Fix-memory-leak-after-calling-xmlXPathWrapNodeSet.patch
Patch6088:  backport-malloc-fail-Fix-memory-leak-in-xmlXIncludeAddNode.patch
Patch6089:  backport-malloc-fail-Fix-memory-leak-after-xmlRegNewState.patch
Patch6090:  backport-malloc-fail-Fix-memory-leak-in-xmlSAX2StartElementNs.patch
Patch6091:  backport-malloc-fail-Fix-memory-leak-in-xmlGetDtdElementDesc2.patch
Patch6092:  backport-malloc-fail-Fix-memory-leak-in-xmlDocDumpFormatMemoryEnc.patch
Patch6093:  backport-malloc-fail-Fix-infinite-loop-in-htmlParseStartTag1.patch
Patch6094:  backport-malloc-fail-Fix-memory-leak-in-xmlXIncludeLoadTxt.patch
Patch6095:  backport-malloc-fail-Fix-memory-leak-in-xmlCopyPropList.patch
Patch6096:  backport-malloc-fail-Fix-memory-leak-after-calling-xmlXPathNodeSetMerge.patch
Patch6097:  backport-malloc-fail-Fix-memory-leak-after-calling-xmlXPathWrapString.patch
Patch6098:  backport-malloc-fail-Fix-memory-leak-in-xmlXPathEqualValuesCommon.patch
Patch6099:  backport-malloc-fail-Fix-memory-leak-in-htmlCreateMemoryParserCtxt.patch
Patch6100:  backport-malloc-fail-Fix-memory-leak-in-htmlCreatePushParserCtxt.patch
Patch6101:  backport-malloc-fail-Fix-infinite-loop-in-htmlParseContentInternal.patch
Patch6102:  backport-malloc-fail-Fix-infinite-loop-in-htmlParseStartTag2.patch
Patch6103:  backport-malloc-fail-Fix-null-deref-in-htmlnamePush.patch
Patch6104:  backport-malloc-fail-Fix-infinite-loop-in-htmlParseDocTypeDecl.patch
Patch6105:  backport-malloc-fail-Fix-error-code-in-htmlParseChunk.patch
Patch6106:  backport-malloc-fail-Fix-memory-leak-in-xmlFAParseCharProp.patch
Patch6107:  backport-malloc-fail-Fix-leak-of-xmlRegAtom.patch
Patch6108:  backport-malloc-fail-Fix-memory-leak-in-xmlRegexpCompile.patch
Patch6109:  backport-malloc-fail-Fix-OOB-read-after-xmlRegGetCounter.patch
Patch6110:  backport-parser-Fix-OOB-read-when-formatting-error-message.patch
Patch6111:  backport-malloc-fail-Fix-memory-leak-in-xmlXPathEqualNodeSetF.patch
Patch6112:  backport-malloc-fail-Fix-use-after-free-related-to-xmlXPathNo.patch
Patch6113:  backport-regexp-Add-sanity-check-in-xmlRegCalloc2.patch
Patch6114:  backport-malloc-fail-Fix-null-deref-in-xmlXPathCompiledEvalIn.patch
Patch6115:  backport-malloc-fail-Fix-null-deref-after-xmlPointerListAddSi.patch
Patch6116:  backport-malloc-fail-Fix-memory-leak-in-xmlGetNsList.patch
Patch6117:  backport-malloc-fail-Check-for-malloc-failure-in-xmlHashAddEn.patch
Patch6118:  backport-malloc-fail-Fix-memory-leak-in-xmlXPathCacheNewNodeS.patch
Patch6119:  backport-malloc-fail-Fix-memory-leak-in-xmlXPathDistinctSorte.patch
Patch6120:  backport-xpath-Fix-harmless-integer-overflow-in-xmlXPathTrans.patch
Patch6121:  backport-malloc-fail-Fix-memory-leak-in-xmlXPathNameFunction.patch
Patch6122:  backport-malloc-fail-Fix-memory-leak-in-xmlSchemaItemListAddS.patch
Patch6123:  backport-malloc-fail-Fix-null-deref-in-xmlGet-Min-Max-Occurs.patch
Patch6124:  backport-malloc-fail-Fix-null-deref-in-xmlSchemaValAtomicType.patch
Patch6125:  backport-malloc-fail-Fix-null-deref-in-xmlSchemaInitTypes.patch
Patch6126:  backport-malloc-fail-Fix-memory-leak-in-xmlSchemaParse.patch
Patch6127:  backport-malloc-fail-Fix-memory-leak-in-xmlCopyNamespaceList.patch
Patch6128:  backport-malloc-fail-Fix-another-memory-leak-in-xmlSchemaBuck.patch
Patch6129:  backport-malloc-fail-Fix-null-deref-in-xmlSchemaParseUnion.patch
Patch6130:  backport-malloc-fail-Fix-memory-leak-in-WXS_ADD_-LOCAL-GLOBAL.patch
Patch6131:  backport-malloc-fail-Fix-memory-leak-in-xmlSchemaBucketCreate.patch
Patch6132:  backport-malloc-fail-Fix-null-deref-in-xmlSchemaParseWildcard.patch
Patch6133:  backport-malloc-fail-Fix-type-confusion-after-xmlSchemaFixupT.patch
Patch6134:  backport-malloc-fail-Fix-null-deref-after-xmlSchemaItemList-A.patch
Patch6135:  backport-malloc-fail-Fix-null-deref-after-xmlSchemaCompareDat.patch
Patch6136:  backport-malloc-fail-Fix-memory-leak-in-xmlSchemaParseUnion.patch
Patch6137:  backport-malloc-fail-Fix-memory-leak-in-xmlXPathRegisterNs.patch
Patch6138:  backport-catalog-Fix-memory-leaks.patch

Patch6139:  backport-CVE-2023-29469.patch
Patch6140:  backport-CVE-2023-28484.patch

Patch6141:  backport-valid-Allow-xmlFreeValidCtxt-NULL.patch
Patch6142:  backport-parser-Use-size_t-when-subtracting-input-buffer-poin.patch
Patch6143:  backport-malloc-fail-Fix-null-deref-in-xmlParserInputShrink.patch
Patch6144:  backport-xmllint-Fix-memory-leak-with-pattern-stream.patch
Patch6145:  backport-xzlib-Fix-implicit-sign-change-in-xz_open.patch
Patch6146:  backport-html-Fix-quadratic-behavior-in-htmlParseTryOrFinish.patch
Patch6147:  backport-valid-Make-xmlValidateElement-non-recursive.patch
Patch6148:  backport-malloc-fail-Fix-buffer-overread-in-htmlParseScript.patch
Patch6149:  backport-malloc-fail-Add-more-error-checks-when-parsing-names.patch
Patch6150:  backport-malloc-fail-Add-error-check-in-htmlParseHTMLAttribut.patch
Patch6151:  backport-parser-Limit-name-length-in-xmlParseEncName.patch
Patch6152:  backport-encoding-Fix-error-code-in-asciiToUTF8.patch
Patch6153:  backport-malloc-fail-Fix-buffer-overread-with-HTML-doctype-de.patch
Patch6154:  backport-parser-Fix-regression-in-xmlParserNodeInfo-accountin.patch
Patch6155:  backport-regexp-Fix-cycle-check-in-xmlFAReduceEpsilonTransiti.patch
Patch6156:  backport-regexp-Fix-checks-for-eliminated-transitions.patch
Patch6157:  backport-regexp-Fix-determinism-checks.patch
Patch6158:  backport-regexp-Fix-mistake-in-previous-commit.patch
Patch6159:  backport-regexp-Fix-null-deref-in-xmlFAFinishReduceEpsilonTra.patch
Patch6160:  backport-hash-Fix-possible-startup-crash-with-old-libxslt-ver.patch
Patch6161:  backport-parser-Fix-old-SAX1-parser-with-custom-callbacks.patch
Patch6162:  backport-xmllint-Fix-use-after-free-with-maxmem.patch
Patch6163:  backport-malloc-fail-Check-for-malloc-failures-when-creating.patch
Patch6164:  backport-malloc-fail-Fix-buffer-overread-after-htmlParseScrip.patch
Patch6165:  backport-xmlValidatePopElement-can-return-invalid-value-1.patch
Patch6166:  backport-Fix-use-after-free-in-xmlParseContentInternal.patch
Patch6167:  backport-malloc-fail-Fix-null-deref-after-xmlXIncludeNewRef.patch

Patch6168:  backport-xpath-Ignore-entity-ref-nodes-when-computing-node-ha.patch
Patch6169:  backport-SAX-Always-initialize-SAX1-element-handlers.patch
Patch6170:  backport-CVE-2023-45322.patch

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

%doc %{_datadir}/doc/libxml2

%{_libdir}/lib*.so.*
%{_bindir}/xmllint
%{_bindir}/xmlcatalog

%files devel
%defattr(-, root, root)

%doc NEWS README.md Copyright
%doc doc/*.html doc/html doc/*.gif doc/*.png
%doc doc/tutorial doc/libxml2-api.xml.gz
%doc doc/examples
%doc %dir %{_datadir}/gtk-doc/html/libxml2
%doc %{_datadir}/gtk-doc/html/libxml2/*.devhelp2
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
* Mon Oct 16 2023 BruceGW <gyl93216@163.com> - 2.9.14-9
- Type:CVE
- CVE:CVE-2023-45322
- SUG:NA
- DESC:fix CVE-2023-45322

* Fri Sep 01 2023 liningjie <liningjie@xfusion.com> - 2.9.14-8
- SAX: Always initialize SAX1 element handlers

* Mon Jun 19 2023 zhuofeng <zhuofeng2@huawei.com> - 2.9.14-7
- Type:bugfix
- CVE:NA
- SUG:NA
- DESC:revert parser-Fix-progress-check

* Thu Jun 08 2023 zhuofeng <zhuofeng2@huawei.com> - 2.9.14-6
- Type:bugfix
- CVE:NA
- SUG:NA
- DESC:backport upstream patches

* Thu Apr 20 2023 BruceGW <gyl93216@163.com> - 2.9.14-5
- Type:CVE
- CVE:CVE-2023-28484 CVE-2023-29469
- SUG:NA
- DESC:fix CVE-2023-28484CVE-2023-29469

* Mon Nov 21 2022 fuanan <fuanan3@h-partners.com> - 2.9.14-4
- Type:bugfix
- CVE:NA
- SUG:NA
- DESC:backport upstream patches

* Tue Nov 08 2022 fuanan <fuanan3@h-partners.com> - 2.9.14-3
- fix CVE-2022-40303 CVE-2022-40304

* Tue Sep 13 2022 fuanan <fuanan3@h-partners.com> - 2.9.14-2
- Fix Obsoletes in spec

* Wed Jul 13 2022 fuanan <fuanan3@h-partners.com> - 2.9.14-1
- Type:enhancement
- ID:NA
- SUG:NA
- DESC:Upgrade to upstream v2.9.14 and Cleanup duplicate installation

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

