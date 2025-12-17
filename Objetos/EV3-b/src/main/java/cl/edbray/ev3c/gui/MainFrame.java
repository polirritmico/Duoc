/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/GUIForms/JFrame.java to edit this template
 */
package cl.edbray.ev3c.gui;

import cl.edbray.ev3c.app.ApplicationContext;
import cl.edbray.ev3c.controller.SwordController;
import cl.edbray.ev3c.model.Sword;
import java.awt.event.KeyAdapter;
import java.awt.event.KeyEvent;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;
import java.util.List;
import java.util.ArrayList;
import javax.swing.JOptionPane;
import javax.swing.ListSelectionModel;
import javax.swing.SwingConstants;
import javax.swing.event.DocumentEvent;
import javax.swing.event.DocumentListener;
import javax.swing.table.AbstractTableModel;
import javax.swing.table.DefaultTableCellRenderer;

/**
 *
 * @author eduardo
 */
public class MainFrame extends javax.swing.JFrame {

    private final SwordController controller;

    private SwordTableModel swordsTableModel;
    private Sword selectedSword;

    private boolean updating = false;

    /**
     * Creates new form MainFrame
     */
    public MainFrame() {
        controller = ApplicationContext.getInstance().getSwordController();

        initComponents();
        setupTable();
        setupButtons();
        setupListeners();

        loadSwords();
        clearDetails();
    }

    private void setupTable() {
        swordsTableModel = new SwordTableModel();
        swordsTable.setModel(swordsTableModel);

        swordsTable.setSelectionMode(ListSelectionModel.SINGLE_SELECTION);

        swordsTable.getColumnModel().getColumn(0).setPreferredWidth(30);
        swordsTable.getColumnModel().getColumn(1).setPreferredWidth(70);

        DefaultTableCellRenderer centerRenderer = new DefaultTableCellRenderer();
        centerRenderer.setHorizontalAlignment(SwingConstants.CENTER);
        swordsTable.getColumnModel().getColumn(0).setCellRenderer(centerRenderer);
        swordsTable.getColumnModel().getColumn(2).setCellRenderer(centerRenderer);
    }

    private void setupButtons() {
        addButton.setEnabled(false);
        cleanButton.setEnabled(false);
    }

    private void setupListeners() {
        swordsTable.getSelectionModel().addListSelectionListener(ev -> {
            if (!ev.getValueIsAdjusting()) {
                selectSwordInTable();
            }
        });

        swordsTable.addMouseListener(new MouseAdapter() {
            @Override
            public void mouseClicked(MouseEvent ev) {
                if (ev.getClickCount() == 2) {
                    selectSwordInTable();
                    materialField.requestFocus();
                    setUpdateState(false);
                }
            }
        });

        materialField.getDocument().addDocumentListener(new DocumentListener() {
            @Override public void insertUpdate(DocumentEvent e) { changed(); }
            @Override public void removeUpdate(DocumentEvent e) { changed(); }
            @Override public void changedUpdate(DocumentEvent e) { changed(); }

            private void changed() {
                if (!updating) {
                    setUpdateState(true);
                }
            }
        });

        lengthField.getDocument().addDocumentListener(new DocumentListener() {
            @Override public void insertUpdate(DocumentEvent e) { changed(); }
            @Override public void removeUpdate(DocumentEvent e) { changed(); }
            @Override public void changedUpdate(DocumentEvent e) { changed(); }

            private void changed() {
                if (!updating) {
                    setUpdateState(true);
                }
            }
        });

        lengthField.addKeyListener(new KeyAdapter() {
            @Override public void keyTyped(KeyEvent ev) {
                if (!Character.isDigit(ev.getKeyChar())) {
                    ev.consume();
                }
            }
        });
    }

    private void loadSwords() {
        List<Sword> swords = controller.listAll();
        swordsTableModel.setSwords(swords);
    }

    private void clearDetails() {
        selectedSword = null;

        swordsTable.clearSelection();
        materialField.setText("");
        lengthField.setText("");

        materialField.requestFocus();
    }

    private void loadInDetails(Sword sword) {
        materialField.setText(sword.getMaterial());
        lengthField.setText(String.valueOf(sword.getLength()));

        setUpdateState(false);
    }

    private void selectSwordInTable() {
        int selectedRow = swordsTable.getSelectedRow();
        if (selectedRow >= 0) {
            selectedSword = swordsTableModel.getSwordAt(selectedRow);
            loadInDetails(selectedSword);
        }
    }

    private void setUpdateState(boolean state) {
        updating = state;
        addButton.setEnabled(state);
        cleanButton.setEnabled(state);
    }

    private void manualReloadMessage() {
        JOptionPane.showMessageDialog(
            this,
            "Se ha vuelto a leer el registro de espadas de la Base de datos",
            "Registro",
            JOptionPane.INFORMATION_MESSAGE
        );
    }

    private void viewButtonActionHandler() {
        clearDetails();
        loadSwords();
        setUpdateState(false);

        manualReloadMessage();
    }

    private void addButtonActionHandler() {
        String material = materialField.getText();
        String lengthText = lengthField.getText();

        try {
            controller.create(material, lengthText);

            JOptionPane.showMessageDialog(
                this,
                "Espada registrada exitosamente.",
                "Éxito",
                JOptionPane.INFORMATION_MESSAGE
            );

            loadSwords();
            clearDetails();

        } catch (RuntimeException e) {
            JOptionPane.showMessageDialog(
                this,
                e.getMessage(),
                "Error",
                JOptionPane.ERROR_MESSAGE
            );
        }
    }

    /**
     * This method is called from within the constructor to initialize the form.
     * WARNING: Do NOT modify this code. The content of this method is always
     * regenerated by the Form Editor.
     */
    @SuppressWarnings("unchecked")
    // <editor-fold defaultstate="collapsed" desc="Generated Code">//GEN-BEGIN:initComponents
    private void initComponents() {
        java.awt.GridBagConstraints gridBagConstraints;

        tablePanel = new javax.swing.JScrollPane();
        swordsTable = new javax.swing.JTable();
        detailsPanel = new javax.swing.JPanel();
        detailsTitleLabel = new javax.swing.JLabel();
        materialLabel = new javax.swing.JLabel();
        materialField = new javax.swing.JTextField();
        lengthLabel = new javax.swing.JLabel();
        lengthField = new javax.swing.JTextField();
        buttonsPanel = new javax.swing.JPanel();
        addButton = new javax.swing.JButton();
        cleanButton = new javax.swing.JButton();
        viewButton = new javax.swing.JButton();

        setDefaultCloseOperation(javax.swing.WindowConstants.EXIT_ON_CLOSE);
        setSize(new java.awt.Dimension(900, 800));
        getContentPane().setLayout(new java.awt.GridBagLayout());

        swordsTable.setModel(new javax.swing.table.DefaultTableModel(
            new Object [][] {
                {null, null, null, null},
                {null, null, null, null},
                {null, null, null, null},
                {null, null, null, null}
            },
            new String [] {
                "Title 1", "Title 2", "Title 3", "Title 4"
            }
        ));
        tablePanel.setViewportView(swordsTable);

        gridBagConstraints = new java.awt.GridBagConstraints();
        gridBagConstraints.fill = java.awt.GridBagConstraints.BOTH;
        gridBagConstraints.weightx = 5.0;
        gridBagConstraints.weighty = 1.0;
        gridBagConstraints.insets = new java.awt.Insets(10, 10, 10, 10);
        getContentPane().add(tablePanel, gridBagConstraints);

        java.awt.GridBagLayout detailsPanelLayout = new java.awt.GridBagLayout();
        detailsPanelLayout.columnWidths = new int[] {0, 5, 0};
        detailsPanelLayout.rowHeights = new int[] {0, 5, 0, 5, 0, 5, 0, 5, 0};
        detailsPanel.setLayout(detailsPanelLayout);

        detailsTitleLabel.setFont(new java.awt.Font("sansserif", 1, 18)); // NOI18N
        detailsTitleLabel.setText("Datos de espada");
        gridBagConstraints = new java.awt.GridBagConstraints();
        gridBagConstraints.gridx = 0;
        gridBagConstraints.gridy = 0;
        gridBagConstraints.gridwidth = 3;
        gridBagConstraints.insets = new java.awt.Insets(0, 0, 40, 0);
        detailsPanel.add(detailsTitleLabel, gridBagConstraints);

        materialLabel.setText("Material:");
        gridBagConstraints = new java.awt.GridBagConstraints();
        gridBagConstraints.gridx = 0;
        gridBagConstraints.gridy = 2;
        detailsPanel.add(materialLabel, gridBagConstraints);
        gridBagConstraints = new java.awt.GridBagConstraints();
        gridBagConstraints.gridx = 2;
        gridBagConstraints.gridy = 2;
        gridBagConstraints.fill = java.awt.GridBagConstraints.HORIZONTAL;
        gridBagConstraints.insets = new java.awt.Insets(0, 5, 0, 0);
        detailsPanel.add(materialField, gridBagConstraints);

        lengthLabel.setText("Longitud:");
        gridBagConstraints = new java.awt.GridBagConstraints();
        gridBagConstraints.gridx = 0;
        gridBagConstraints.gridy = 4;
        detailsPanel.add(lengthLabel, gridBagConstraints);
        gridBagConstraints = new java.awt.GridBagConstraints();
        gridBagConstraints.gridx = 2;
        gridBagConstraints.gridy = 4;
        gridBagConstraints.fill = java.awt.GridBagConstraints.HORIZONTAL;
        gridBagConstraints.insets = new java.awt.Insets(0, 5, 0, 0);
        detailsPanel.add(lengthField, gridBagConstraints);

        buttonsPanel.setLayout(new java.awt.GridLayout(2, 2, 10, 10));

        addButton.setText("Agregar");
        addButton.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                addButtonActionPerformed(evt);
            }
        });
        buttonsPanel.add(addButton);

        cleanButton.setText("Limpiar");
        cleanButton.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                cleanButtonActionPerformed(evt);
            }
        });
        buttonsPanel.add(cleanButton);

        viewButton.setText("Ver Registros");
        viewButton.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                viewButtonActionPerformed(evt);
            }
        });
        buttonsPanel.add(viewButton);

        gridBagConstraints = new java.awt.GridBagConstraints();
        gridBagConstraints.gridx = 0;
        gridBagConstraints.gridy = 6;
        gridBagConstraints.gridwidth = 3;
        gridBagConstraints.fill = java.awt.GridBagConstraints.HORIZONTAL;
        gridBagConstraints.insets = new java.awt.Insets(25, 5, 0, 5);
        detailsPanel.add(buttonsPanel, gridBagConstraints);

        gridBagConstraints = new java.awt.GridBagConstraints();
        gridBagConstraints.fill = java.awt.GridBagConstraints.HORIZONTAL;
        gridBagConstraints.anchor = java.awt.GridBagConstraints.NORTH;
        gridBagConstraints.weightx = 5.0;
        gridBagConstraints.weighty = 1.0;
        gridBagConstraints.insets = new java.awt.Insets(30, 0, 10, 0);
        getContentPane().add(detailsPanel, gridBagConstraints);

        pack();
    }// </editor-fold>//GEN-END:initComponents

    private void cleanButtonActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_cleanButtonActionPerformed
        clearDetails();
    }//GEN-LAST:event_cleanButtonActionPerformed

    private void viewButtonActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_viewButtonActionPerformed
        viewButtonActionHandler();
    }//GEN-LAST:event_viewButtonActionPerformed

    private void addButtonActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_addButtonActionPerformed
        addButtonActionHandler();
    }//GEN-LAST:event_addButtonActionPerformed

    /**
     * @param args the command line arguments
     */
    public static void main(String args[]) {
        /* Set the Nimbus look and feel */
        //<editor-fold defaultstate="collapsed" desc=" Look and feel setting code (optional) ">
        /* If Nimbus (introduced in Java SE 6) is not available, stay with the default look and feel.
         * For details see http://download.oracle.com/javase/tutorial/uiswing/lookandfeel/plaf.html
         */
        try {
            for (javax.swing.UIManager.LookAndFeelInfo info : javax.swing.UIManager.getInstalledLookAndFeels()) {
                if ("Nimbus".equals(info.getName())) {
                    javax.swing.UIManager.setLookAndFeel(info.getClassName());
                    break;
                }
            }
        } catch (ClassNotFoundException ex) {
            java.util.logging.Logger.getLogger(MainFrame.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (InstantiationException ex) {
            java.util.logging.Logger.getLogger(MainFrame.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (IllegalAccessException ex) {
            java.util.logging.Logger.getLogger(MainFrame.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (javax.swing.UnsupportedLookAndFeelException ex) {
            java.util.logging.Logger.getLogger(MainFrame.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        }
        //</editor-fold>

        /* Create and display the form */
        java.awt.EventQueue.invokeLater(new Runnable() {
            public void run() {
                new MainFrame().setVisible(true);
            }
        });
    }

    // Variables declaration - do not modify//GEN-BEGIN:variables
    private javax.swing.JButton addButton;
    private javax.swing.JPanel buttonsPanel;
    private javax.swing.JButton cleanButton;
    private javax.swing.JPanel detailsPanel;
    private javax.swing.JLabel detailsTitleLabel;
    private javax.swing.JTextField lengthField;
    private javax.swing.JLabel lengthLabel;
    private javax.swing.JTextField materialField;
    private javax.swing.JLabel materialLabel;
    private javax.swing.JTable swordsTable;
    private javax.swing.JScrollPane tablePanel;
    private javax.swing.JButton viewButton;
    // End of variables declaration//GEN-END:variables

    private class SwordTableModel extends AbstractTableModel {
        private List<Sword> swords = new ArrayList<>();
        private final String[] columnNames = {"ID", "Material", "Longitud"};

        public void setSwords(List<Sword> swords) {
            this.swords = swords;
            fireTableDataChanged();
        }

        public Sword getSwordAt(int row) {
            return swords.get(row);
        }

        @Override
        public int getRowCount() {
            return swords.size();
        }

        @Override
        public String getColumnName(int column) {
            return columnNames[column];
        }

        @Override
        public int getColumnCount() {
            return columnNames.length;
        }

        @Override
        public Object getValueAt(int row, int col) {
            Sword s = swords.get(row);
            return switch (col) {
                case 0 -> s.getId();
                case 1 -> s.getMaterial();
                case 2 -> s.getLength();
                default -> null;
            };
        }


    }
}
