import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

class Toy {
    private String name;
    private double price;

    public Toy(String name, double price) {
        this.name = name;
        this.price = price;
    }

    public String getName() {
        return name;
    }

    public double getPrice() {
        return price;
    }
}

class ToyShop {
    private List<Toy> toys;

    public ToyShop() {
        toys = new ArrayList<>();
    }

    public void addToy(Toy toy) {
        toys.add(toy);
    }

    public void displayToys() {
        System.out.println("Игрушки в магазине:");
        for (Toy toy : toys) {
            System.out.println(toy.getName() + " - Цена: " + toy.getPrice());
        }
    }

    public double calculateTotalPrice() {
        double totalPrice = 0.0;
        for (Toy toy : toys) {
            totalPrice += toy.getPrice();
        }
        return totalPrice;
    }
}

public class ToyStore {
    public static void main(String[] args) {
        ToyShop toyShop = new ToyShop();

        // Добавляем игрушки в магазин
        toyShop.addToy(new Toy("Мишка Тедди", 7.99));
        toyShop.addToy(new Toy("Кукла Барби", 12.99));
        toyShop.addToy(new Toy("Машинка Hot Wheels", 5.49));

        // Отображаем игрушки в магазине
        toyShop.displayToys();

        // Вычисляем общую стоимость игрушек
        double totalPrice = toyShop.calculateTotalPrice();
        System.out.println("Общая стоимость игрушек в магазине: " + totalPrice);
    }
}