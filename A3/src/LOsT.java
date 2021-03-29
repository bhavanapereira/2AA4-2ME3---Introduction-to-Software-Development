package src;

public class LOsT implements Measures{

	private String name;
	private int n_blw;
	private int n_mrg;
	private int n_mts;
	private int n_exc;


	public LOsT(String topic, int nblw, int nmrg, int nmts, int nexc){
		if (nblw <= 0 || nmrg <= 0 || nmts <= 0 || nexc <= 0){
			throw new IllegalArgumentException("Illegal Argument Exception");
		}
		else{
			this.name = topic;
			this.n_blw = nblw;
			this.n_mrg = nmrg;
			this.n_mts = nmts;
			this.n_exc = nexc;
		}
	}

	public String getName(){
		return name;
	}

	public Boolean equals(LOsT o){
		return name == o.getName();
	}

	public double[] measures(){
		double[] array = new double[4];
		array[0] = n_blw;
		array[1] = n_mrg;
		array[2] = n_mts;
		array[3] = n_exc;
		if (Norm.getNLOs() == false){
			return array;
		}
		else{
			return Services.normal(array);
		}
	}

	public double[] measures (IndicatorT ind){
		throw new UnsupportedOperationException("Unsupported Operation Exception");
	}

	public double[] measures(AttributeT att){
		throw new UnsupportedOperationException("Unsupported Operation Exception");
	}
}