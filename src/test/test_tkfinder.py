import unittest, json
from src import tkfinder

kazuya = {
    "name": "kazuya",
    "proper_name": "Kazuya",
    "local_json": "kazuya.json",
    "online_webpage": "http://rbnorway.org/kazuya-t7-frames",
    "portrait": "https://i.imgur.com/kMvhDfU.jpg"
}


class MyTestCase(unittest.TestCase):
    def test_get_commands(self):
        result = tkfinder.get_commands_from("hwoarang")
        self.assertIn("1,1,3,3", result)

    def test_get_generic(self):
        result = tkfinder.get_generic_move("d+4")
        self.assertEqual("-13", result["Block frame"])

    def test_ganryu_gigas(self):
        gan = {
            "local_json": "ganryu.json",
            "name": "ganryu",
            "online_webpage": "",
            "portrait": "https://i.imgur.com/6kScGMT.png",
            "proper_name": "Ganryu"
        }

        self.assertEqual("b+1~2", tkfinder.get_move(gan, "b1~2")["Command"])
        gigas =   {
            "local_json": "gigas.json",
            "name": "gigas",
            "online_webpage": "http://geppopotamus.info/game/tekken7fr/gigas/data_en.htm",
            "portrait": "https://i.imgur.com/jTGmJyf.jpg",
            "proper_name": "Gigas"
        }

        self.assertEqual("RD (3 steps) b+2*~f,n", tkfinder.get_move(gigas, "RD (3 steps) b+2*~f,n")["Command"])


    def test_get_close_moves(self):
        close_moves = tkfinder.get_similar_moves("d/f+1,2", "hwoarang")
        self.assertIn("d/f+1,3", close_moves)

    def test_is_command_in_alias(self):
        item = {'Alias': ["hs", "hellsweep", "Giant swing", "u/f3"]}
        result = tkfinder.is_command_in_alias("hellsweep", item)
        self.assertTrue(result)

        result = tkfinder.is_command_in_alias("he", item)
        self.assertFalse(result)

        result = tkfinder.is_command_in_alias("uf3", item)
        self.assertTrue(result)

    def test_get_cha_name(self):
        result = tkfinder.correct_character_name("hwoarang")
        self.assertEqual("hwoarang", result)

        result = tkfinder.correct_character_name("hwo")
        self.assertEqual("hwoarang", result)

        result = tkfinder.correct_character_name("kazu")
        self.assertEqual(None, result)

    def test_get_move_by_type(self):
        self.assertIn("in rage f,n,d,d/f+1+4", tkfinder.get_by_move_type(kazuya, "Rage Drive"))
        self.assertIn("d/f+2", tkfinder.get_by_move_type(kazuya, "Homing"))
        self.assertIn("2,2", tkfinder.get_by_move_type(kazuya, "Screw"))
        self.assertIn("f+2", tkfinder.get_by_move_type(kazuya, "Power Crush"))
        self.assertIn("f,F+1+2", tkfinder.get_by_move_type(kazuya, "Throw"))
        self.assertIn("f+1+2", tkfinder.get_by_move_type(kazuya, "Wall Bounce"))
        self.assertIn("in rage d/f+1+2", tkfinder.get_by_move_type(kazuya, "Rage Art"))

    def test_get_recovery(self):
        paul = {
            "local_json": "paul.json",
            "name": "paul",
            "online_webpage": "http://rbnorway.org/paul-t7-frames",
            "portrait": "https://i.imgur.com/vbjcEy1.jpg",
            "proper_name": "Paul"
        }

        self.assertEqual("-37", tkfinder.get_move(paul, "qcf2")["Recovery"])
        move = tkfinder.get_move(paul, "d3")
        self.assertFalse('Recovery' in move)

    def test_get_cha_move(self):
        jin = {
            "local_json": "jin.json",
            "name": "jin",
            "online_webpage": "http://rbnorway.org/jin-t7-frames",
            "portrait": "https://i.imgur.com/xat3qAS.jpg",
            "proper_name": "Jin"
        }
        self.assertEqual("in rage f,n,d,d/f+1+2", tkfinder.get_move(jin, "in rage cd 1+2")["Command"])

        leroy = {
            "local_json": "leroy.json",
            "name": "leroy",
            "online_webpage": "",
            "portrait": "https://i.imgur.com/FrR8dDq.png",
            "proper_name": "Leroy Smith"
        }
        self.assertEqual("d/f+1", tkfinder.get_move(leroy, "df1")["Command"])
        self.assertEqual("f,f,f+3", tkfinder.get_move(kazuya, "wr3")["Command"])
        self.assertEqual("1,1,2", tkfinder.get_move(kazuya, "112")["Command"])
        self.assertEqual("f,n,d,d/f+4,1", tkfinder.get_move(kazuya, "hs")["Command"])
        self.assertEqual("f,n,d,d/f+4,1", tkfinder.get_move(kazuya, "cd41")["Command"])
        self.assertEqual("f,n,d,d/f:2", tkfinder.get_move(kazuya, "ewgf")["Command"])
        self.assertEqual("WS 1,2", tkfinder.get_move(kazuya, "ws12")["Command"])
        self.assertEqual("b+2,1", tkfinder.get_move(kazuya, "b21")["Command"])
        marduk = {
            "name": "marduk",
            "proper_name": "Marduk",
            "local_json": "marduk.json",
            "online_webpage": "http://rbnorway.org/marduk-t7-frames",
            "portrait": "https://i.imgur.com/2OtX6nd.png"
        }
        self.assertEqual("d/f+3,d/f+1,2", tkfinder.get_move(marduk, "df3df12")["Command"])
        self.assertEqual("d/f+3,1,d+2", tkfinder.get_move(marduk, "df31,d+2")["Command"])
        self.assertEqual("d/f+3,1,d+2", tkfinder.get_move(marduk, "df3,1d+2")["Command"])
        self.assertEqual("d/f+3,1,d+2", tkfinder.get_move(marduk, "df+3,1d2")["Command"])
        self.assertEqual("(u/b_u_u/f)+3", tkfinder.get_move(marduk, "u3")["Command"])
        self.assertEqual("(u/b_u_u/f)+3", tkfinder.get_move(marduk, "uf3")["Command"])
        self.assertEqual("(u/b_u_u/f)+3", tkfinder.get_move(marduk, "ub3")["Command"])

        leo = {
            "name": "leo",
            "proper_name": "Leo",
            "local_json": "leo.json",
            "online_webpage": "http://rbnorway.org/leo-t7-frames",
            "portrait": "https://i.imgur.com/i1CO8SB.jpg"
        }
        self.assertEqual("WS 4,1+2", tkfinder.get_move(leo, "ws41+2")["Command"])
        self.assertEqual("b+1,4", tkfinder.get_move(leo, "b14")["Command"])
        self.assertEqual("KNK 3,4", tkfinder.get_move(leo, "knk 34")["Command"])
        self.assertEqual("KNK 1+2", tkfinder.get_move(leo, "knk 1+2")["Command"])
        self.assertEqual("FC d/f+3", tkfinder.get_move(leo, "fc df3")["Command"])
        kazumi = {
            "name": "kazumi",
            "proper_name": "Kazumi",
            "local_json": "kazumi.json",
            "online_webpage": "http://rbnorway.org/kazumi-t7-frames",
            "portrait": "https://i.imgur.com/ZNiaFwL.jpg"
        }
        self.assertEqual("b,f+2,1,1+2", tkfinder.get_move(kazumi, "bf211+2")["Command"])
        self.assertEqual("u/f+4", tkfinder.get_move(kazumi, "uf4")["Command"])

        chloe = {
            "name": "lucky_chloe",
            "proper_name": "Lucky Chloe",
            "local_json": "lucky_chloe.json",
            "online_webpage": "http://rbnorway.org/lucky-chloe-t7-frames",
            "portrait": "https://i.imgur.com/iNXYpwT.jpg"
        }
        self.assertEqual("u/f+3", tkfinder.get_move(chloe, "uf3")["Command"])

        leroy = {
            "local_json": "leroy.json",
            "name": "leroy",
            "online_webpage": "",
            "portrait": "https://i.imgur.com/FrR8dDq.png",
            "proper_name": "Leroy Smith"
        }

        self.assertEqual("HRM 3,4", tkfinder.get_move(leroy, "HRM 34")["Command"])

    def test_ling(self):
        ling = {
            "name": "xiaoyu",
            "proper_name": "Xiaoyu",
            "local_json": "xiaoyu.json",
            "online_webpage": "http://rbnorway.org/xiaoyu-t7-frames",
            "portrait": "https://i.imgur.com/zuojLtJ.jpg"
        }
        self.assertEqual("AOP u/f+3,3", tkfinder.get_move(ling, "AOP uf33")["Command"])
        self.assertEqual("AOP u/f+3,3", tkfinder.get_move(ling, "AOP ub33")["Command"])
        self.assertEqual("AOP u/f+3,3", tkfinder.get_move(ling, "AOP u33")["Command"])

    def test_hwo(self):
        hwo = {
            "local_json": "hwoarang.json",
            "name": "hwoarang",
            "online_webpage": "http://rbnorway.org/hwoarang-t7-frames",
            "portrait": "https://i.imgur.com/rCx49Yl.jpg",
            "proper_name": "Hwoarang"
        }
        self.assertIn("d/f+3", tkfinder.get_by_move_type(hwo, "Power Crush"))

    def test_move_simplifier(self):
        move = "wr3"
        self.assertEqual("fff3", tkfinder.move_simplifier(move))

        move = "df+3,df+1,1+2"
        self.assertEqual("df3df11+2", tkfinder.move_simplifier(move))

    def test_none(self):
        entry1 = json.loads("[{\"Gif\": \"\"}]")
        entry2 = json.loads("[{\"Gif\": \"something\"}]")
        entry3 = json.loads("[{\"Gif\": null}]")
        entry4 = json.loads("[{\"Test\": \"test\"}]")

        self.assertTrue(not entry1[0]["Gif"])
        self.assertTrue(entry2[0]["Gif"])
        self.assertTrue(not entry3[0]["Gif"])
        self.assertTrue(not 'Gif' in entry4)


if __name__ == '__main__':
    unittest.main()
