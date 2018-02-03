package com.example.jahnvi.myfirstapp;

import android.graphics.Bitmap;
import android.graphics.BitmapFactory;
import android.os.Environment;
import android.util.Log;

import org.jcodec.api.android.AndroidSequenceEncoder;
import org.jcodec.common.io.NIOUtils;
import org.jcodec.common.io.SeekableByteChannel;
import org.jcodec.common.model.Rational;

import java.io.File;
import java.io.IOException;

/**
 * Created by jahnvi on 30/9/17.
 */

public class CreateMP4fromImages {
    public void getVideo(){
        SeekableByteChannel out = null;
        try {
            File path = Environment.getExternalStoragePublicDirectory(
                    Environment.DIRECTORY_PICTURES);

            out = NIOUtils.writableFileChannel(path.toString() + "/output.mp4");
            // for Android use: AndroidSequenceEncoder
            AndroidSequenceEncoder encoder = new AndroidSequenceEncoder(out, Rational.R(1, 1));
            for (int i = 1; i<=3;i++) {
                BitmapFactory.Options options = new BitmapFactory.Options();
                options.inJustDecodeBounds = true;

//Returns null, sizes are in the options variable
                BitmapFactory.decodeFile(path.toString()+"/"+i+".png", options);
                Integer width = options.outWidth;
                Integer height = options.outHeight;
                Log.e("Check********* ",width.toString());
                Log.e("Check********* ",height.toString());
                // Generate the image, for Android use Bitmap
                Bitmap image = BitmapFactory.decodeFile(path.toString()+"/"+i+".png");
                if(width%2 == 1) width--;
                if(height%2 == 1) height--;
                image = scaleDown(image, width, height, true);
                // Encode the image
                Integer w = image.getWidth();
                Log.e("Let's see---> ", w.toString());
                encoder.encodeImage(image);
            }
            // Finalize the encoding, i.e. clear the buffers, write the header, etc.
            encoder.finish();
        } catch (IOException e) {
            Log.e("msg----------- ",e.toString());
            e.printStackTrace();
        }
        finally {
            NIOUtils.closeQuietly(out);
        }
    }

    public static Bitmap scaleDown(Bitmap realImage, int width, int height,
                                   boolean filter) {

        Bitmap newBitmap = Bitmap.createScaledBitmap(realImage, width,
                height, filter);
        return newBitmap;
    }
}
