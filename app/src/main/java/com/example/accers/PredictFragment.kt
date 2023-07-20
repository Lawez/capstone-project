package com.example.accers

import android.app.*
import android.content.Context
import android.content.Context.NOTIFICATION_SERVICE
import android.content.Intent
import android.graphics.BitmapFactory
import android.graphics.Color
import android.os.Build
import android.os.Bundle
import android.util.Log
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.ArrayAdapter
import android.widget.Button
import android.widget.EditText
import android.widget.Spinner
import android.widget.TextView
import android.widget.Toast
import androidx.core.content.ContextCompat.getSystemService
import androidx.fragment.app.Fragment
import com.android.volley.Response
import com.android.volley.VolleyError
import com.android.volley.toolbox.StringRequest
import com.android.volley.toolbox.Volley
import com.example.accers.R
import org.json.JSONException
import org.json.JSONObject

class PredictFragment : Fragment() {

    private val genderOptions = arrayOf("Male", "Female")
    private val weatherOptions = arrayOf("Rainy", "Sunny", "Cloudy")
    private val caloriesOptions = arrayOf(
        "100 and Below",
        "101 to 200",
        "201 to 300",
        "301 to 400",
        "401 to 500",
        "501 to 600",
        "601 to 700",
        "701 to 800",
        "801 and Above"
    )

    override fun onCreateView(inflater: LayoutInflater, container: ViewGroup?, savedInstanceState: Bundle?): View? {
        val view = inflater.inflate(R.layout.fragment_predict, container, false)

        val button: Button = view.findViewById(R.id.predict)
        val result: TextView = view.findViewById(R.id.result)
        val dreamWeight: EditText = view.findViewById(R.id.editDweight)
        val age: EditText = view.findViewById(R.id.editAge)
        val actualWeight: EditText = view.findViewById(R.id.editAweight)
        val height: EditText = view.findViewById(R.id.editheight)
        val duration: EditText = view.findViewById(R.id.editduration)
        val genderSpinner: Spinner = view.findViewById(R.id.genderSpinner)
        val weatherSpinner: Spinner = view.findViewById(R.id.weatherSpinner)
        val caloriesSpinner: Spinner = view.findViewById(R.id.caloriesSpinner)

        // Setup adapters for the spinners
        val genderAdapter = ArrayAdapter(requireContext(), android.R.layout.simple_spinner_item, genderOptions)
        genderAdapter.setDropDownViewResource(android.R.layout.simple_spinner_dropdown_item)
        genderSpinner.adapter = genderAdapter

        val weatherAdapter = ArrayAdapter(requireContext(), android.R.layout.simple_spinner_item, weatherOptions)
        weatherAdapter.setDropDownViewResource(android.R.layout.simple_spinner_dropdown_item)
        weatherSpinner.adapter = weatherAdapter

        val caloriesAdapter = ArrayAdapter(requireContext(), android.R.layout.simple_spinner_item, caloriesOptions)
        caloriesAdapter.setDropDownViewResource(android.R.layout.simple_spinner_dropdown_item)
        caloriesSpinner.adapter = caloriesAdapter

        button.setOnClickListener {
            val url = "https://android-flask-codes-raw-11b4cf0ebe42.herokuapp.com/predict" // Replace "YOUR_FLASK_API_URL" with the actual URL of your Flask API

            val queue = Volley.newRequestQueue(activity)
            val stringRequest = object : StringRequest(Method.POST, url,
                Response.Listener { response ->
                    try {
                        val jsonObject = JSONObject(response)
                        val intensity = jsonObject.getInt("intensity")
                        val description = jsonObject.getString("description")
                        val heartRate = jsonObject.getInt("heart_rate")

                        result.text = "Intensity: $intensity\n\n Max-Heart Rate: $heartRate\n Description: $description"
                    } catch (e: JSONException) {
                        e.printStackTrace()
                    }
                },
                Response.ErrorListener { error ->
                    onErrorResponse(error)
                }) {
                override fun getParams(): MutableMap<String, String>? {
                    val params: MutableMap<String, String> = HashMap()

                    params["calorie_range"] = caloriesSpinner.selectedItem.toString()
                    params["dream_weight"] = dreamWeight.text.toString()
                    params["actual_weight"] = actualWeight.text.toString()
                    params["age"] = age.text.toString()
                    params["duration"] = duration.text.toString()
                    params["height"] = height.text.toString()
                    params["weather_conditions"] = weatherSpinner.selectedItem.toString()
                    params["gender"] = genderSpinner.selectedItem.toString()

                    return params
                }
            }

            queue.add(stringRequest)
        }

        return view
    }

    private fun onErrorResponse(error: VolleyError) {
        Log.e("TAG", "RESPONSE IS $error")
        Toast.makeText(activity, "Failed to get response", Toast.LENGTH_SHORT).show()
    }
}
