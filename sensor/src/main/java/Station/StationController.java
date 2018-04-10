package Station;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.ResponseBody;

import Station.Stationtable;
import Station.StationRepository;

@Controller    // This means that this class is a Controller
@RequestMapping(path="/sensor") // This means URL's start with /demo (after Application path)

public class StationController {
    @Autowired // This means to get the bean called userRepository
    // Which is auto-generated by Spring, we will use it to handle the data
    private StationRepository stationRepository;
    @GetMapping(path="/adddata") // Map ONLY GET Requests
    public @ResponseBody String addNewData (@RequestParam String Parameter_Name
            , @RequestParam String Date_Recorded) {
        // @ResponseBody means the returned String is the response, not a view name
        // @RequestParam means it is a parameter from the GET or POST request
        Stationtable s = new Stationtable();
        s.setparameter_Name(Parameter_Name);
        s.setDate_Recorder(Date_Recorded);
        stationRepository.save(s);
        return "Saved";
    }
    @GetMapping(path="/displaydata")
    public @ResponseBody Iterable<Stationtable> getAllData() {
        // This returns a JSON or XML with the users
        return stationRepository.findAll();
    }


}
