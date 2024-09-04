package expertsystemsactivity;

public class mainbanana {
    private int str = 0;
    private int intl = 0;
    private int dex = 0;
    private int end = 0;
    private int cha = 0;
    private int agi = 0;
    private int fai = 0;

    public mainbanana(int str, int intl, int dex, int end, int cha, int agi, int fai) {
        this.str = str;
        this.intl = intl;
        this.dex = dex;
        this.end = end;
        this.cha = cha;
        this.agi = agi;
        this.fai = fai;
    }

    public mainbanana() {}

    public void setStr(int str) {
        this.str = str;
    }
    public void setIntl(int intl) {
        this.intl = intl;
    }
    public void setDex(int dex) {
        this.dex = dex;
    }
    public void setEnd(int end) {
        this.end = end;
    }
    public void setCha(int cha) {
        this.cha = cha;
    }
    public void setAgi(int agi) {
        this.agi = agi;
    }
    public void setFai(int fai) {
        this.fai = fai;
    }

    public int getStr() {
        return str;
    }
    public int getIntl() {
        return intl;
    }
    public int getDex() {
        return dex;
    }
    public int getEnd() {
        return end;
    }
    public int getCha() {
        return cha;
    }
    public int getAgi() {
        return agi;
    }
    public int getFai() {
        return fai;
    }

    
}
