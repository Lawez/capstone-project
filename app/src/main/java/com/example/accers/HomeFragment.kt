import android.os.Bundle
import androidx.fragment.app.Fragment
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.TextView
import com.example.accers.R

class HomeFragment : Fragment() {

    override fun onCreateView(inflater: LayoutInflater, container: ViewGroup?, savedInstanceState: Bundle?): View? {
        val view = inflater.inflate(R.layout.fragment_home, container, false)

        val resultTextView: TextView = view.findViewById(R.id.resultTextView)

        // Check if there are results passed from the PredictFragment
        arguments?.let { bundle ->
            val intensity = bundle.getInt("intensity")
            val description = bundle.getString("description")
            val heartRate = bundle.getInt("heartRate")

            // Display the results in the views
            resultTextView.text = "Intensity: $intensity\nDescription: $description\nHeart Rate: $heartRate"
        }

        return view
    }

}