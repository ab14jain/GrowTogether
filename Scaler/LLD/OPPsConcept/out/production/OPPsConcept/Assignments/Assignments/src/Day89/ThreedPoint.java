package Day89;

public class ThreedPoint {
    private int z;

    public void display(){
        Point p = new Point();
        System.out.println("[<<" + p.x + ">>,<<" + p.y + ">>,<<" + this.z + ">>]");
    }

    public int getter(){
        return this.z;
    }

    public void setter(int z){
        this.z = z;
    }
}

