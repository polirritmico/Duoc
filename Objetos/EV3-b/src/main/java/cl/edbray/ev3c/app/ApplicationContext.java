/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package cl.edbray.ev3c.app;

import cl.edbray.ev3c.controller.SwordController;
import cl.edbray.ev3c.repository.SwordRepository;
import cl.edbray.ev3c.repository.impl.SwordRepositoryMysql;
import cl.edbray.ev3c.service.SwordService;
import cl.edbray.ev3c.utils.MysqlDBConnectionFactory;

/**
 *
 * @author eduardo
 */
public class ApplicationContext {

    private static ApplicationContext instance;

    private SwordRepository swordRepository;
    private SwordService swordService;
    private SwordController swordController;

    private ApplicationContext() {
        init();
    }

    public static ApplicationContext getInstance(){
        if (instance == null) {
            instance = new ApplicationContext();
        }
        return instance;
    }

    private void init() {
        System.out.println("Initializating ApplicationContext...");

        swordRepository = new SwordRepositoryMysql();
        swordService = new SwordService(swordRepository);
        swordController = new SwordController(swordService);

        System.out.println("ApplicationContext initialization success");
    }

    public SwordController getSwordController() {
        return swordController;
    }

    public static void reset() {
        instance = null;
    }
}
