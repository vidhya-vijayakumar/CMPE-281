package Station;

import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;

public class Stationtable {

    @Id
    @GeneratedValue(strategy=GenerationType.AUTO)
    private Integer Sample_Duration;

    private String Parameter_Name;

    private String Date_Recorded;

    public Integer Observation_Count;

    public Integer Observation_percent;

    private String Site_Name;

    private String Site_Address;

    private String Site_State;

    private String County;

    private String City_Name;



    public Integer getsample_Duration() {
        return Sample_Duration;
    }

    public void setsample_Duration(Integer Sample_Duration) {
        this.Sample_Duration = Sample_Duration;
    }

    public String getparameter_Name() {
        return Parameter_Name;
    }

    public void setparameter_Name(String Parameter_Name) {
        this.Parameter_Name = Parameter_Name;
    }

    public String getdate_Recorder() {
        return Date_Recorded;
    }

    public void setDate_Recorder(String Date_Recorder) {
        this.Date_Recorded = Date_Recorder;
    }




}

