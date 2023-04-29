---
layout: post
title: "A review of ruby s3 librarys"
date: 2008-05-31T16:43:47
tags: [ruby]
---

#### [gem install s3sync](http://s3sync.net/wiki)

Has the right idea about how to store files, but the lib it uses does not abstract things enough. Does not use http keep alive to avoid the slow startup of tcp. Does not have an easy way to iterate over all keys in a bucket, but this helps to do this:

      def each_object(bucket_name)
        next_marker = nil
        while true do
          response = CONN.list_bucket(bucket_name, {'marker' => next_marker, 'max-keys' => 10})
          response.entries.each do |s3obj|
            yield s3obj
          end
          break unless response.properties.is_truncated
          next_marker = response.entries.last.key
        end
      end

#### [gem install aws-s3](http://amazon.rubyforge.org/)

Again no built in way to iterate over all keys. Has problems with '/' at the start of file names.

#### [gem install right_aws](http://rightaws.rubyforge.org/)

Uses the same http connection, can iterate over all keys with a single method (though, it makes a full array of all the keys rather than allowing you to supply a block). Here's my thumbnailer:

      require 'rubygems'
      require 'right_aws'
      require 'RMagick'
      require 'pp'

      s3 = RightAws::S3.new(AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY)

      picture_bucket = s3.bucket('OurPictures')
      thumbnail_bucket = s3.bucket('OurPicturesThumbnails')

      picture_bucket.keys.each do |key|
        thumbnail_key = RightAws::S3::Key.create(thumbnail_bucket, key.name)
        next if key.name !~ /.jpg$/i
        next if thumbnail_key.exists?
        image = Magick::Image.from_blob(key.data).first
        image.change_geometry!('256x256>') do |cols, rows, img|
          img.thumbnail!(cols, rows)
        end
        thumbnail_key.put(image.to_blob, 'private')
        p thumbnail_key.full_name
        image = nil
        GC.start
      end
