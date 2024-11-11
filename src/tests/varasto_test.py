'''test'''

import unittest
from varasto import Varasto

# t o d o    actually have something useful in the docstrings

class TestVarasto(unittest.TestCase):
    '''test class'''

    def setUp(self):
        '''a'''
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        '''a'''
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        '''a'''
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        '''a'''
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        '''a'''
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        '''a'''
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        '''a'''
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_a(self):
        '''a'''
        self.varasto.lisaa_varastoon(4)
        q = self.varasto.ota_varastosta(5)
        self.assertEqual(q, 4)

    def test_aa(self):
        '''a'''
        self.varasto.lisaa_varastoon(1)
        q = self.varasto.ota_varastosta(-2)
        self.assertEqual(q, 0)

    def test_b(self):
        '''a'''
        self.varasto.lisaa_varastoon(11)
        self.assertEqual(self.varasto.saldo, 10)

    def test_c(self):
        '''a'''
        self.varasto.lisaa_varastoon(-22)
        self.assertEqual(self.varasto.saldo, 0)

    def test_d(self):
        '''a'''
        q = Varasto(-1)
        self.assertEqual(q.tilavuus, 0)

    def test_e(self):
        '''a'''
        q = Varasto(1, -2)
        self.assertEqual(q.saldo, 0)

    def test_f(self):
        '''a'''
        self.assertEqual(str(self.varasto), 'saldo = 0, vielä tilaa 10')
