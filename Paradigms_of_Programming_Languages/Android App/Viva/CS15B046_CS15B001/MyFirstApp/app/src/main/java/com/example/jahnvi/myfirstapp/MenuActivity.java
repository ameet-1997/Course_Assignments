package com.example.jahnvi.myfirstapp;

import android.content.Intent;
import android.graphics.Typeface;
import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;

public class MenuActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_menu);
        TextView text = (TextView) findViewById(R.id.submit_text_view_id);
        Typeface tf = Typeface.createFromAsset(getAssets(), "fonts/Quicksand-Bold.otf");
        text.setTypeface(tf);

        Button mButton = (Button)findViewById(R.id.submit);
        final EditText mEdit   = (EditText) findViewById(R.id.num_input);

        mButton.setOnClickListener(
                new View.OnClickListener()
                {
                    public void onClick(View view)
                    {
                        Intent intent = new Intent(MenuActivity.this, VideoActivity.class); // runtime binding between separate components
                        Integer maxInputNum = 0;
                        try {
                            maxInputNum = Integer.parseInt(mEdit.getText().toString());
                        }
                        catch(Exception e){}
                        intent.putExtra("N",maxInputNum);
                        startActivity(intent);
                        Log.v("EditText", mEdit.getText().toString());
                    }
                });

    }

}
