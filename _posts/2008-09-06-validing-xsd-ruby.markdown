---
layout: post
title: "Validing with an XSD in ruby"
date: 2008-09-06T20:06:42
tags: []
---


        xml = generate_xml
        require 'xml'
        Tempfile.open(self.class.to_s) do |tmp|
          tmp.write(xml)
          tmp.close
          document = XML::Document.file(tmp.path)
          schema_doc = XML::Document.file("some.xsd")
          schema = XML::Schema.document(schema_doc)
          assert document.validate(schema), "the xml isn't valid.  look above for error."
        end
    


