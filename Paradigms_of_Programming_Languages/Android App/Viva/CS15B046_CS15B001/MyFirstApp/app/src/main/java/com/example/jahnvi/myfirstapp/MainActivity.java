package com.example.jahnvi.myfirstapp;

import android.content.Intent;
import android.graphics.Typeface;
import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.widget.ListView;
import android.widget.SeekBar;
import android.widget.TextView;

import java.util.Timer;

public class MainActivity extends AppCompatActivity {
    private int currImage = 1;
    Timer timer;
    boolean pause = false;
    SeekBar seekBar1;
    private ListView mListView;
    int turns = 0;

    @Override
    protected void onCreate(Bundle savedInstanceState) {

        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        TextView text = (TextView) findViewById(R.id.app_id);
        Typeface tf = Typeface.createFromAsset(getAssets(), "fonts/Quicksand-Bold.otf");
        text.setTypeface(tf);
        new android.os.Handler().postDelayed(new Runnable() {
            @Override
            public void run() {

                Intent i=new Intent(MainActivity.this,InstActivity.class);
                startActivity(i);
            }
        }, 2000);

    }


}
