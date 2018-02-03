package com.example.jahnvi.myfirstapp;

import android.graphics.Bitmap;
import android.graphics.BitmapFactory;
import android.graphics.Canvas;
import android.graphics.Color;
import android.graphics.Paint;
import android.os.Bundle;
import android.os.Environment;
import android.support.v7.app.AppCompatActivity;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.ImageView;
import android.widget.SeekBar;
import android.widget.TextView;

import com.github.clans.fab.FloatingActionButton;

import java.io.File;
import java.util.Timer;
import java.util.TimerTask;

public class VideoActivity extends AppCompatActivity {
    private int currImage = 1;
    Timer timer;
    boolean pause = false;
    SeekBar seekBar1;
    TextView progressText;
    FloatingActionButton menu1,menu2,menu3 ;
    int period = 1000/24;
    private int total = 880;        // What does it do? Shouldn't it be saved from previous activity?
    int drawableId;
    Bitmap image;
    private boolean setNormalForward = true;        // is this the old fast forward?
    Thread thread ;
    private boolean setNormalBackward = true;
    File path = Environment.getExternalStoragePublicDirectory(
            Environment.DIRECTORY_PICTURES);



    @Override
    protected void onCreate(Bundle savedInstanceState) {
        int n = getIntent().getIntExtra("N",0);
        total = n;
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_video);
        menu1 = (FloatingActionButton)findViewById(R.id.subFloatingMenu1) ;
        menu1.setImageBitmap(textAsBitmap("x 0.5", 18, Color.WHITE));
        menu2 = (FloatingActionButton)findViewById(R.id.subFloatingMenu2) ;
        menu2.setImageBitmap(textAsBitmap("x 1", 18, Color.WHITE));
        menu3 = (FloatingActionButton)findViewById(R.id.subFloatingMenu3) ;
        menu3.setImageBitmap(textAsBitmap("x 2", 18, Color.WHITE));

        menu1.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {

                timer.cancel();
                period = 1000/12;
                timer = new Timer();
                int delay = 0;
                timer.scheduleAtFixedRate(new TimerTask() {
                    public void run() {
                        thread = new Thread(new Runnable() {
                            public void run() {
                                Log.e("fps ", setNormalForward+" "+setNormalBackward + " " + currImage);

                                if (!pause)
                                    if (setNormalForward && setNormalBackward) currImage++;
                                    else if(!setNormalForward) currImage += 3;
                                    else currImage -= 2;
                                if (currImage<1) currImage = total;
                                if (currImage > total) {
                                    currImage = 1;
                                }
                                setPlayPauseListener();
                                setFastForwardListener();
                                setFastBackwardListener();
                                if(!pause) {
                                    int progress = (currImage * 100) / total;
                                    seekBar1.setProgress(progress);
                                }
                                try {
                                    runOnUiThread(new Runnable() {
                                        @Override
                                        public void run() {

                                            if (!pause) {
                                                setCurrentImage();
                                            }

                                        }
                                    });
                                } catch (Exception e) {
                                }
                            }
                        });
                        thread.start();
                    }
                }, delay, period);
            }
        });

        menu2.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                timer.cancel();
                period = 1000/24;
                timer = new Timer();
                int delay = 0;
                timer.scheduleAtFixedRate(new TimerTask() {
                    public void run() {
                        thread = new Thread(new Runnable() {
                            public void run() {
                                Log.e("fps ", setNormalForward+" "+setNormalBackward + " " + currImage);

                                if (!pause)
                                    if (setNormalForward && setNormalBackward) currImage++;
                                    else if(!setNormalForward) currImage += 3;
                                    else currImage -= 2;
                                if (currImage<1) currImage = total;
                                if (currImage > total) {
                                    currImage = 1;
                                }
                                setPlayPauseListener();
                                setFastForwardListener();
                                setFastBackwardListener();
                                if(!pause) {
                                    int progress = (currImage * 100) / total;
                                    seekBar1.setProgress(progress);
                                }
                                try {
                                    runOnUiThread(new Runnable() {  //You have to use runOnUiThread() when you want to update your UI from a Non-UI Thread.
                                        @Override
                                        public void run() {

                                            if (!pause) {
                                                setCurrentImage();
                                            }

                                        }
                                    });
                                } catch (Exception e) {
                                }
                            }
                        });
                        thread.start();
                    }
                }, delay, period);
            }
        });

        menu3.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                timer.cancel();
                period = 1000/24;       // Why is it the same as before?
                timer = new Timer();
                int delay = 0;
                timer.scheduleAtFixedRate(new TimerTask() {
                    public void run() {
                        thread = new Thread(new Runnable() {
                            public void run() {
                                Log.e("fps ", setNormalForward+" "+setNormalBackward + " " + currImage);

                                if (!pause)
                                    if (setNormalForward && setNormalBackward) currImage+=2;
                                    else if(!setNormalForward) currImage += 3;
                                    else currImage -= 2;
                                if (currImage<1) currImage = total;
                                if (currImage > total) {
                                    currImage = 1;
                                }
                                setPlayPauseListener();
                                setFastForwardListener();
                                setFastBackwardListener();
                                if(!pause) {
                                    int progress = (currImage * 100) / total;
                                    seekBar1.setProgress(progress);
                                }
                                try {
                                    runOnUiThread(new Runnable() {
                                        @Override
                                        public void run() {

                                            if (!pause) {
                                                setCurrentImage();
                                            }

                                        }
                                    });
                                } catch (Exception e) {
                                }
                            }
                        });
                        thread.start();
                    }
                }, delay, period);
            }
        });

        seekBar1=(SeekBar)findViewById(R.id.seekBar1);
        progressText=(TextView)findViewById(R.id.progressText);
        seekBar1.setOnSeekBarChangeListener(new SeekBar.OnSeekBarChangeListener()
        {

            public void onStopTrackingTouch(SeekBar bar)
            {
                int value = bar.getProgress(); // the value of the seekBar progress
            }

            public void onStartTrackingTouch(SeekBar bar)
            {

            }

            public void onProgressChanged(SeekBar bar,
                                          int paramInt, boolean paramBoolean)
            {
                seekBar1.setProgress(paramInt);
                currImage = (paramInt*total)/100;
                setCurrentImage();
                int val = (paramInt * (seekBar1.getWidth() - 2 * seekBar1.getThumbOffset())) / seekBar1.getMax();
                int secs = (paramInt*total)/2500;   // Why the division by 2500?
                int mins = secs/60;
                secs -= (mins*60);
                String minutes = ""+mins, seconds = ""+secs;
                if(secs<10) seconds = "0"+secs;         // Adding a 0 to make it 2 digits
                if(mins<10) minutes = "0"+mins;
                progressText.setText(minutes+":" + seconds);
                progressText.setX(seekBar1.getX() + val + seekBar1.getThumbOffset() / 2);
            }
        });
        setInitialImage();

            timer = new Timer();
            int delay = 1000;           // Difference between delay and period
                                        // The globally defined period will be used here
            timer.scheduleAtFixedRate(new TimerTask() {
                public void run() {
                    thread = new Thread(new Runnable() {
                        public void run() {
                            Log.e("fps ", setNormalForward+" "+setNormalBackward + " " + currImage);

                            if (!pause)
                                if (setNormalForward && setNormalBackward) currImage++;
                                else if(!setNormalForward) currImage += 3;
                                else currImage -= 2;
                            if (currImage<1) currImage = total;
                            if (currImage > total) {
                                currImage = 1;
                            }
                            setPlayPauseListener();
                            setFastForwardListener();
                            setFastBackwardListener();
                            if(!pause) {
                                int progress = (currImage * 100) / total;
                                seekBar1.setProgress(progress);
                            }
                            try {
                                runOnUiThread(new Runnable() {
                                    @Override
                                    public void run() {

                                        if (!pause) {
                                            setCurrentImage();
                                        }

                                    }
                                });
                            } catch (Exception e) {
                            }
                        }
                    });
                    thread.start();
                }
            }, delay, period);
    }
    public static Bitmap textAsBitmap(String text, float textSize, int textColor) {
        Paint paint = new Paint(Paint.ANTI_ALIAS_FLAG);
        paint.setTextSize(textSize);
        paint.setColor(textColor);
        paint.setTextAlign(Paint.Align.LEFT);
        float baseline = -paint.ascent(); // ascent() is negative
        int width = (int) (paint.measureText(text) + 0.0f); // round
        int height = (int) (baseline + paint.descent() + 0.0f);
        Bitmap image = Bitmap.createBitmap(width, height, Bitmap.Config.ARGB_8888);

        Canvas canvas = new Canvas(image);
        canvas.drawText(text, 0, baseline, paint);
        return image;
    }


    private void setPlayPauseListener() {
        final Button rotatebutton = (Button) findViewById(R.id.btnPlayPause);
        rotatebutton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View arg0) {
                Log.v("3 ","click");
                pause = !pause;
                if(pause) {setNormalForward=true; setNormalBackward=true;}
                if(!pause)
                    rotatebutton.setBackgroundResource(R.drawable.pause);       // Change the image being displayed
                else
                    rotatebutton.setBackgroundResource(R.drawable.play);
            }
        });
    }
    private void setFastForwardListener() {
        final Button rotatebutton = (Button) findViewById(R.id.btnFastForward);
        rotatebutton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View arg0) {
                    setNormalForward = false;
                    setNormalBackward = true;
            }});
    }
    private void setFastBackwardListener() {
        final Button rotatebutton = (Button) findViewById(R.id.btnFastBackward);
        rotatebutton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View arg0) {
                setNormalForward = true;
                setNormalBackward = false;
            }});
    }

    private void setInitialImage() {
        setCurrentImage();
    }

    private void setCurrentImage() {
        final ImageView imageView = (ImageView) findViewById(R.id.iv);
        if (currImage<1) currImage = total;
        image = BitmapFactory.decodeFile(path.toString()+"/"+currImage+".jpg");
        imageView.setImageBitmap(image);
    }

    @Override
    public void onDestroy() {       // Destroying the activity
        thread.interrupt();
        super.onDestroy();
    }
    @Override
    public void onBackPressed() {
        timer.cancel();
        thread.interrupt();
        super.onBackPressed();
    }
}
