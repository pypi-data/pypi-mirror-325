function un(e) {
  return e.replace(/(^|_)(\w)/g, (t, n, r, i) => i === 0 ? r.toLowerCase() : r.toUpperCase());
}
var ht = typeof global == "object" && global && global.Object === Object && global, ln = typeof self == "object" && self && self.Object === Object && self, S = ht || ln || Function("return this")(), w = S.Symbol, yt = Object.prototype, cn = yt.hasOwnProperty, fn = yt.toString, Y = w ? w.toStringTag : void 0;
function pn(e) {
  var t = cn.call(e, Y), n = e[Y];
  try {
    e[Y] = void 0;
    var r = !0;
  } catch {
  }
  var i = fn.call(e);
  return r && (t ? e[Y] = n : delete e[Y]), i;
}
var gn = Object.prototype, dn = gn.toString;
function _n(e) {
  return dn.call(e);
}
var bn = "[object Null]", hn = "[object Undefined]", Ue = w ? w.toStringTag : void 0;
function K(e) {
  return e == null ? e === void 0 ? hn : bn : Ue && Ue in Object(e) ? pn(e) : _n(e);
}
function E(e) {
  return e != null && typeof e == "object";
}
var yn = "[object Symbol]";
function Te(e) {
  return typeof e == "symbol" || E(e) && K(e) == yn;
}
function mt(e, t) {
  for (var n = -1, r = e == null ? 0 : e.length, i = Array(r); ++n < r; )
    i[n] = t(e[n], n, e);
  return i;
}
var P = Array.isArray, mn = 1 / 0, Ge = w ? w.prototype : void 0, Be = Ge ? Ge.toString : void 0;
function vt(e) {
  if (typeof e == "string")
    return e;
  if (P(e))
    return mt(e, vt) + "";
  if (Te(e))
    return Be ? Be.call(e) : "";
  var t = e + "";
  return t == "0" && 1 / e == -mn ? "-0" : t;
}
function q(e) {
  var t = typeof e;
  return e != null && (t == "object" || t == "function");
}
function Tt(e) {
  return e;
}
var vn = "[object AsyncFunction]", Tn = "[object Function]", $n = "[object GeneratorFunction]", wn = "[object Proxy]";
function $t(e) {
  if (!q(e))
    return !1;
  var t = K(e);
  return t == Tn || t == $n || t == vn || t == wn;
}
var pe = S["__core-js_shared__"], ze = function() {
  var e = /[^.]+$/.exec(pe && pe.keys && pe.keys.IE_PROTO || "");
  return e ? "Symbol(src)_1." + e : "";
}();
function On(e) {
  return !!ze && ze in e;
}
var Pn = Function.prototype, An = Pn.toString;
function U(e) {
  if (e != null) {
    try {
      return An.call(e);
    } catch {
    }
    try {
      return e + "";
    } catch {
    }
  }
  return "";
}
var Sn = /[\\^$.*+?()[\]{}|]/g, xn = /^\[object .+?Constructor\]$/, Cn = Function.prototype, En = Object.prototype, jn = Cn.toString, In = En.hasOwnProperty, Mn = RegExp("^" + jn.call(In).replace(Sn, "\\$&").replace(/hasOwnProperty|(function).*?(?=\\\()| for .+?(?=\\\])/g, "$1.*?") + "$");
function Fn(e) {
  if (!q(e) || On(e))
    return !1;
  var t = $t(e) ? Mn : xn;
  return t.test(U(e));
}
function Ln(e, t) {
  return e == null ? void 0 : e[t];
}
function G(e, t) {
  var n = Ln(e, t);
  return Fn(n) ? n : void 0;
}
var be = G(S, "WeakMap"), He = Object.create, Rn = /* @__PURE__ */ function() {
  function e() {
  }
  return function(t) {
    if (!q(t))
      return {};
    if (He)
      return He(t);
    e.prototype = t;
    var n = new e();
    return e.prototype = void 0, n;
  };
}();
function Nn(e, t, n) {
  switch (n.length) {
    case 0:
      return e.call(t);
    case 1:
      return e.call(t, n[0]);
    case 2:
      return e.call(t, n[0], n[1]);
    case 3:
      return e.call(t, n[0], n[1], n[2]);
  }
  return e.apply(t, n);
}
function Dn(e, t) {
  var n = -1, r = e.length;
  for (t || (t = Array(r)); ++n < r; )
    t[n] = e[n];
  return t;
}
var Kn = 800, Un = 16, Gn = Date.now;
function Bn(e) {
  var t = 0, n = 0;
  return function() {
    var r = Gn(), i = Un - (r - n);
    if (n = r, i > 0) {
      if (++t >= Kn)
        return arguments[0];
    } else
      t = 0;
    return e.apply(void 0, arguments);
  };
}
function zn(e) {
  return function() {
    return e;
  };
}
var re = function() {
  try {
    var e = G(Object, "defineProperty");
    return e({}, "", {}), e;
  } catch {
  }
}(), Hn = re ? function(e, t) {
  return re(e, "toString", {
    configurable: !0,
    enumerable: !1,
    value: zn(t),
    writable: !0
  });
} : Tt, qn = Bn(Hn);
function Yn(e, t) {
  for (var n = -1, r = e == null ? 0 : e.length; ++n < r && t(e[n], n, e) !== !1; )
    ;
  return e;
}
var Xn = 9007199254740991, Jn = /^(?:0|[1-9]\d*)$/;
function wt(e, t) {
  var n = typeof e;
  return t = t ?? Xn, !!t && (n == "number" || n != "symbol" && Jn.test(e)) && e > -1 && e % 1 == 0 && e < t;
}
function $e(e, t, n) {
  t == "__proto__" && re ? re(e, t, {
    configurable: !0,
    enumerable: !0,
    value: n,
    writable: !0
  }) : e[t] = n;
}
function we(e, t) {
  return e === t || e !== e && t !== t;
}
var Zn = Object.prototype, Wn = Zn.hasOwnProperty;
function Ot(e, t, n) {
  var r = e[t];
  (!(Wn.call(e, t) && we(r, n)) || n === void 0 && !(t in e)) && $e(e, t, n);
}
function W(e, t, n, r) {
  var i = !n;
  n || (n = {});
  for (var o = -1, a = t.length; ++o < a; ) {
    var s = t[o], u = void 0;
    u === void 0 && (u = e[s]), i ? $e(n, s, u) : Ot(n, s, u);
  }
  return n;
}
var qe = Math.max;
function Qn(e, t, n) {
  return t = qe(t === void 0 ? e.length - 1 : t, 0), function() {
    for (var r = arguments, i = -1, o = qe(r.length - t, 0), a = Array(o); ++i < o; )
      a[i] = r[t + i];
    i = -1;
    for (var s = Array(t + 1); ++i < t; )
      s[i] = r[i];
    return s[t] = n(a), Nn(e, this, s);
  };
}
var Vn = 9007199254740991;
function Oe(e) {
  return typeof e == "number" && e > -1 && e % 1 == 0 && e <= Vn;
}
function Pt(e) {
  return e != null && Oe(e.length) && !$t(e);
}
var kn = Object.prototype;
function Pe(e) {
  var t = e && e.constructor, n = typeof t == "function" && t.prototype || kn;
  return e === n;
}
function er(e, t) {
  for (var n = -1, r = Array(e); ++n < e; )
    r[n] = t(n);
  return r;
}
var tr = "[object Arguments]";
function Ye(e) {
  return E(e) && K(e) == tr;
}
var At = Object.prototype, nr = At.hasOwnProperty, rr = At.propertyIsEnumerable, Ae = Ye(/* @__PURE__ */ function() {
  return arguments;
}()) ? Ye : function(e) {
  return E(e) && nr.call(e, "callee") && !rr.call(e, "callee");
};
function ir() {
  return !1;
}
var St = typeof exports == "object" && exports && !exports.nodeType && exports, Xe = St && typeof module == "object" && module && !module.nodeType && module, or = Xe && Xe.exports === St, Je = or ? S.Buffer : void 0, ar = Je ? Je.isBuffer : void 0, ie = ar || ir, sr = "[object Arguments]", ur = "[object Array]", lr = "[object Boolean]", cr = "[object Date]", fr = "[object Error]", pr = "[object Function]", gr = "[object Map]", dr = "[object Number]", _r = "[object Object]", br = "[object RegExp]", hr = "[object Set]", yr = "[object String]", mr = "[object WeakMap]", vr = "[object ArrayBuffer]", Tr = "[object DataView]", $r = "[object Float32Array]", wr = "[object Float64Array]", Or = "[object Int8Array]", Pr = "[object Int16Array]", Ar = "[object Int32Array]", Sr = "[object Uint8Array]", xr = "[object Uint8ClampedArray]", Cr = "[object Uint16Array]", Er = "[object Uint32Array]", y = {};
y[$r] = y[wr] = y[Or] = y[Pr] = y[Ar] = y[Sr] = y[xr] = y[Cr] = y[Er] = !0;
y[sr] = y[ur] = y[vr] = y[lr] = y[Tr] = y[cr] = y[fr] = y[pr] = y[gr] = y[dr] = y[_r] = y[br] = y[hr] = y[yr] = y[mr] = !1;
function jr(e) {
  return E(e) && Oe(e.length) && !!y[K(e)];
}
function Se(e) {
  return function(t) {
    return e(t);
  };
}
var xt = typeof exports == "object" && exports && !exports.nodeType && exports, X = xt && typeof module == "object" && module && !module.nodeType && module, Ir = X && X.exports === xt, ge = Ir && ht.process, z = function() {
  try {
    var e = X && X.require && X.require("util").types;
    return e || ge && ge.binding && ge.binding("util");
  } catch {
  }
}(), Ze = z && z.isTypedArray, Ct = Ze ? Se(Ze) : jr, Mr = Object.prototype, Fr = Mr.hasOwnProperty;
function Et(e, t) {
  var n = P(e), r = !n && Ae(e), i = !n && !r && ie(e), o = !n && !r && !i && Ct(e), a = n || r || i || o, s = a ? er(e.length, String) : [], u = s.length;
  for (var l in e)
    (t || Fr.call(e, l)) && !(a && // Safari 9 has enumerable `arguments.length` in strict mode.
    (l == "length" || // Node.js 0.10 has enumerable non-index properties on buffers.
    i && (l == "offset" || l == "parent") || // PhantomJS 2 has enumerable non-index properties on typed arrays.
    o && (l == "buffer" || l == "byteLength" || l == "byteOffset") || // Skip index properties.
    wt(l, u))) && s.push(l);
  return s;
}
function jt(e, t) {
  return function(n) {
    return e(t(n));
  };
}
var Lr = jt(Object.keys, Object), Rr = Object.prototype, Nr = Rr.hasOwnProperty;
function Dr(e) {
  if (!Pe(e))
    return Lr(e);
  var t = [];
  for (var n in Object(e))
    Nr.call(e, n) && n != "constructor" && t.push(n);
  return t;
}
function Q(e) {
  return Pt(e) ? Et(e) : Dr(e);
}
function Kr(e) {
  var t = [];
  if (e != null)
    for (var n in Object(e))
      t.push(n);
  return t;
}
var Ur = Object.prototype, Gr = Ur.hasOwnProperty;
function Br(e) {
  if (!q(e))
    return Kr(e);
  var t = Pe(e), n = [];
  for (var r in e)
    r == "constructor" && (t || !Gr.call(e, r)) || n.push(r);
  return n;
}
function xe(e) {
  return Pt(e) ? Et(e, !0) : Br(e);
}
var zr = /\.|\[(?:[^[\]]*|(["'])(?:(?!\1)[^\\]|\\.)*?\1)\]/, Hr = /^\w*$/;
function Ce(e, t) {
  if (P(e))
    return !1;
  var n = typeof e;
  return n == "number" || n == "symbol" || n == "boolean" || e == null || Te(e) ? !0 : Hr.test(e) || !zr.test(e) || t != null && e in Object(t);
}
var J = G(Object, "create");
function qr() {
  this.__data__ = J ? J(null) : {}, this.size = 0;
}
function Yr(e) {
  var t = this.has(e) && delete this.__data__[e];
  return this.size -= t ? 1 : 0, t;
}
var Xr = "__lodash_hash_undefined__", Jr = Object.prototype, Zr = Jr.hasOwnProperty;
function Wr(e) {
  var t = this.__data__;
  if (J) {
    var n = t[e];
    return n === Xr ? void 0 : n;
  }
  return Zr.call(t, e) ? t[e] : void 0;
}
var Qr = Object.prototype, Vr = Qr.hasOwnProperty;
function kr(e) {
  var t = this.__data__;
  return J ? t[e] !== void 0 : Vr.call(t, e);
}
var ei = "__lodash_hash_undefined__";
function ti(e, t) {
  var n = this.__data__;
  return this.size += this.has(e) ? 0 : 1, n[e] = J && t === void 0 ? ei : t, this;
}
function D(e) {
  var t = -1, n = e == null ? 0 : e.length;
  for (this.clear(); ++t < n; ) {
    var r = e[t];
    this.set(r[0], r[1]);
  }
}
D.prototype.clear = qr;
D.prototype.delete = Yr;
D.prototype.get = Wr;
D.prototype.has = kr;
D.prototype.set = ti;
function ni() {
  this.__data__ = [], this.size = 0;
}
function ue(e, t) {
  for (var n = e.length; n--; )
    if (we(e[n][0], t))
      return n;
  return -1;
}
var ri = Array.prototype, ii = ri.splice;
function oi(e) {
  var t = this.__data__, n = ue(t, e);
  if (n < 0)
    return !1;
  var r = t.length - 1;
  return n == r ? t.pop() : ii.call(t, n, 1), --this.size, !0;
}
function ai(e) {
  var t = this.__data__, n = ue(t, e);
  return n < 0 ? void 0 : t[n][1];
}
function si(e) {
  return ue(this.__data__, e) > -1;
}
function ui(e, t) {
  var n = this.__data__, r = ue(n, e);
  return r < 0 ? (++this.size, n.push([e, t])) : n[r][1] = t, this;
}
function j(e) {
  var t = -1, n = e == null ? 0 : e.length;
  for (this.clear(); ++t < n; ) {
    var r = e[t];
    this.set(r[0], r[1]);
  }
}
j.prototype.clear = ni;
j.prototype.delete = oi;
j.prototype.get = ai;
j.prototype.has = si;
j.prototype.set = ui;
var Z = G(S, "Map");
function li() {
  this.size = 0, this.__data__ = {
    hash: new D(),
    map: new (Z || j)(),
    string: new D()
  };
}
function ci(e) {
  var t = typeof e;
  return t == "string" || t == "number" || t == "symbol" || t == "boolean" ? e !== "__proto__" : e === null;
}
function le(e, t) {
  var n = e.__data__;
  return ci(t) ? n[typeof t == "string" ? "string" : "hash"] : n.map;
}
function fi(e) {
  var t = le(this, e).delete(e);
  return this.size -= t ? 1 : 0, t;
}
function pi(e) {
  return le(this, e).get(e);
}
function gi(e) {
  return le(this, e).has(e);
}
function di(e, t) {
  var n = le(this, e), r = n.size;
  return n.set(e, t), this.size += n.size == r ? 0 : 1, this;
}
function I(e) {
  var t = -1, n = e == null ? 0 : e.length;
  for (this.clear(); ++t < n; ) {
    var r = e[t];
    this.set(r[0], r[1]);
  }
}
I.prototype.clear = li;
I.prototype.delete = fi;
I.prototype.get = pi;
I.prototype.has = gi;
I.prototype.set = di;
var _i = "Expected a function";
function Ee(e, t) {
  if (typeof e != "function" || t != null && typeof t != "function")
    throw new TypeError(_i);
  var n = function() {
    var r = arguments, i = t ? t.apply(this, r) : r[0], o = n.cache;
    if (o.has(i))
      return o.get(i);
    var a = e.apply(this, r);
    return n.cache = o.set(i, a) || o, a;
  };
  return n.cache = new (Ee.Cache || I)(), n;
}
Ee.Cache = I;
var bi = 500;
function hi(e) {
  var t = Ee(e, function(r) {
    return n.size === bi && n.clear(), r;
  }), n = t.cache;
  return t;
}
var yi = /[^.[\]]+|\[(?:(-?\d+(?:\.\d+)?)|(["'])((?:(?!\2)[^\\]|\\.)*?)\2)\]|(?=(?:\.|\[\])(?:\.|\[\]|$))/g, mi = /\\(\\)?/g, vi = hi(function(e) {
  var t = [];
  return e.charCodeAt(0) === 46 && t.push(""), e.replace(yi, function(n, r, i, o) {
    t.push(i ? o.replace(mi, "$1") : r || n);
  }), t;
});
function Ti(e) {
  return e == null ? "" : vt(e);
}
function ce(e, t) {
  return P(e) ? e : Ce(e, t) ? [e] : vi(Ti(e));
}
var $i = 1 / 0;
function V(e) {
  if (typeof e == "string" || Te(e))
    return e;
  var t = e + "";
  return t == "0" && 1 / e == -$i ? "-0" : t;
}
function je(e, t) {
  t = ce(t, e);
  for (var n = 0, r = t.length; e != null && n < r; )
    e = e[V(t[n++])];
  return n && n == r ? e : void 0;
}
function wi(e, t, n) {
  var r = e == null ? void 0 : je(e, t);
  return r === void 0 ? n : r;
}
function Ie(e, t) {
  for (var n = -1, r = t.length, i = e.length; ++n < r; )
    e[i + n] = t[n];
  return e;
}
var We = w ? w.isConcatSpreadable : void 0;
function Oi(e) {
  return P(e) || Ae(e) || !!(We && e && e[We]);
}
function Pi(e, t, n, r, i) {
  var o = -1, a = e.length;
  for (n || (n = Oi), i || (i = []); ++o < a; ) {
    var s = e[o];
    n(s) ? Ie(i, s) : i[i.length] = s;
  }
  return i;
}
function Ai(e) {
  var t = e == null ? 0 : e.length;
  return t ? Pi(e) : [];
}
function Si(e) {
  return qn(Qn(e, void 0, Ai), e + "");
}
var Me = jt(Object.getPrototypeOf, Object), xi = "[object Object]", Ci = Function.prototype, Ei = Object.prototype, It = Ci.toString, ji = Ei.hasOwnProperty, Ii = It.call(Object);
function Mi(e) {
  if (!E(e) || K(e) != xi)
    return !1;
  var t = Me(e);
  if (t === null)
    return !0;
  var n = ji.call(t, "constructor") && t.constructor;
  return typeof n == "function" && n instanceof n && It.call(n) == Ii;
}
function Fi(e, t, n) {
  var r = -1, i = e.length;
  t < 0 && (t = -t > i ? 0 : i + t), n = n > i ? i : n, n < 0 && (n += i), i = t > n ? 0 : n - t >>> 0, t >>>= 0;
  for (var o = Array(i); ++r < i; )
    o[r] = e[r + t];
  return o;
}
function Li() {
  this.__data__ = new j(), this.size = 0;
}
function Ri(e) {
  var t = this.__data__, n = t.delete(e);
  return this.size = t.size, n;
}
function Ni(e) {
  return this.__data__.get(e);
}
function Di(e) {
  return this.__data__.has(e);
}
var Ki = 200;
function Ui(e, t) {
  var n = this.__data__;
  if (n instanceof j) {
    var r = n.__data__;
    if (!Z || r.length < Ki - 1)
      return r.push([e, t]), this.size = ++n.size, this;
    n = this.__data__ = new I(r);
  }
  return n.set(e, t), this.size = n.size, this;
}
function A(e) {
  var t = this.__data__ = new j(e);
  this.size = t.size;
}
A.prototype.clear = Li;
A.prototype.delete = Ri;
A.prototype.get = Ni;
A.prototype.has = Di;
A.prototype.set = Ui;
function Gi(e, t) {
  return e && W(t, Q(t), e);
}
function Bi(e, t) {
  return e && W(t, xe(t), e);
}
var Mt = typeof exports == "object" && exports && !exports.nodeType && exports, Qe = Mt && typeof module == "object" && module && !module.nodeType && module, zi = Qe && Qe.exports === Mt, Ve = zi ? S.Buffer : void 0, ke = Ve ? Ve.allocUnsafe : void 0;
function Hi(e, t) {
  if (t)
    return e.slice();
  var n = e.length, r = ke ? ke(n) : new e.constructor(n);
  return e.copy(r), r;
}
function qi(e, t) {
  for (var n = -1, r = e == null ? 0 : e.length, i = 0, o = []; ++n < r; ) {
    var a = e[n];
    t(a, n, e) && (o[i++] = a);
  }
  return o;
}
function Ft() {
  return [];
}
var Yi = Object.prototype, Xi = Yi.propertyIsEnumerable, et = Object.getOwnPropertySymbols, Fe = et ? function(e) {
  return e == null ? [] : (e = Object(e), qi(et(e), function(t) {
    return Xi.call(e, t);
  }));
} : Ft;
function Ji(e, t) {
  return W(e, Fe(e), t);
}
var Zi = Object.getOwnPropertySymbols, Lt = Zi ? function(e) {
  for (var t = []; e; )
    Ie(t, Fe(e)), e = Me(e);
  return t;
} : Ft;
function Wi(e, t) {
  return W(e, Lt(e), t);
}
function Rt(e, t, n) {
  var r = t(e);
  return P(e) ? r : Ie(r, n(e));
}
function he(e) {
  return Rt(e, Q, Fe);
}
function Nt(e) {
  return Rt(e, xe, Lt);
}
var ye = G(S, "DataView"), me = G(S, "Promise"), ve = G(S, "Set"), tt = "[object Map]", Qi = "[object Object]", nt = "[object Promise]", rt = "[object Set]", it = "[object WeakMap]", ot = "[object DataView]", Vi = U(ye), ki = U(Z), eo = U(me), to = U(ve), no = U(be), O = K;
(ye && O(new ye(new ArrayBuffer(1))) != ot || Z && O(new Z()) != tt || me && O(me.resolve()) != nt || ve && O(new ve()) != rt || be && O(new be()) != it) && (O = function(e) {
  var t = K(e), n = t == Qi ? e.constructor : void 0, r = n ? U(n) : "";
  if (r)
    switch (r) {
      case Vi:
        return ot;
      case ki:
        return tt;
      case eo:
        return nt;
      case to:
        return rt;
      case no:
        return it;
    }
  return t;
});
var ro = Object.prototype, io = ro.hasOwnProperty;
function oo(e) {
  var t = e.length, n = new e.constructor(t);
  return t && typeof e[0] == "string" && io.call(e, "index") && (n.index = e.index, n.input = e.input), n;
}
var oe = S.Uint8Array;
function Le(e) {
  var t = new e.constructor(e.byteLength);
  return new oe(t).set(new oe(e)), t;
}
function ao(e, t) {
  var n = t ? Le(e.buffer) : e.buffer;
  return new e.constructor(n, e.byteOffset, e.byteLength);
}
var so = /\w*$/;
function uo(e) {
  var t = new e.constructor(e.source, so.exec(e));
  return t.lastIndex = e.lastIndex, t;
}
var at = w ? w.prototype : void 0, st = at ? at.valueOf : void 0;
function lo(e) {
  return st ? Object(st.call(e)) : {};
}
function co(e, t) {
  var n = t ? Le(e.buffer) : e.buffer;
  return new e.constructor(n, e.byteOffset, e.length);
}
var fo = "[object Boolean]", po = "[object Date]", go = "[object Map]", _o = "[object Number]", bo = "[object RegExp]", ho = "[object Set]", yo = "[object String]", mo = "[object Symbol]", vo = "[object ArrayBuffer]", To = "[object DataView]", $o = "[object Float32Array]", wo = "[object Float64Array]", Oo = "[object Int8Array]", Po = "[object Int16Array]", Ao = "[object Int32Array]", So = "[object Uint8Array]", xo = "[object Uint8ClampedArray]", Co = "[object Uint16Array]", Eo = "[object Uint32Array]";
function jo(e, t, n) {
  var r = e.constructor;
  switch (t) {
    case vo:
      return Le(e);
    case fo:
    case po:
      return new r(+e);
    case To:
      return ao(e, n);
    case $o:
    case wo:
    case Oo:
    case Po:
    case Ao:
    case So:
    case xo:
    case Co:
    case Eo:
      return co(e, n);
    case go:
      return new r();
    case _o:
    case yo:
      return new r(e);
    case bo:
      return uo(e);
    case ho:
      return new r();
    case mo:
      return lo(e);
  }
}
function Io(e) {
  return typeof e.constructor == "function" && !Pe(e) ? Rn(Me(e)) : {};
}
var Mo = "[object Map]";
function Fo(e) {
  return E(e) && O(e) == Mo;
}
var ut = z && z.isMap, Lo = ut ? Se(ut) : Fo, Ro = "[object Set]";
function No(e) {
  return E(e) && O(e) == Ro;
}
var lt = z && z.isSet, Do = lt ? Se(lt) : No, Ko = 1, Uo = 2, Go = 4, Dt = "[object Arguments]", Bo = "[object Array]", zo = "[object Boolean]", Ho = "[object Date]", qo = "[object Error]", Kt = "[object Function]", Yo = "[object GeneratorFunction]", Xo = "[object Map]", Jo = "[object Number]", Ut = "[object Object]", Zo = "[object RegExp]", Wo = "[object Set]", Qo = "[object String]", Vo = "[object Symbol]", ko = "[object WeakMap]", ea = "[object ArrayBuffer]", ta = "[object DataView]", na = "[object Float32Array]", ra = "[object Float64Array]", ia = "[object Int8Array]", oa = "[object Int16Array]", aa = "[object Int32Array]", sa = "[object Uint8Array]", ua = "[object Uint8ClampedArray]", la = "[object Uint16Array]", ca = "[object Uint32Array]", h = {};
h[Dt] = h[Bo] = h[ea] = h[ta] = h[zo] = h[Ho] = h[na] = h[ra] = h[ia] = h[oa] = h[aa] = h[Xo] = h[Jo] = h[Ut] = h[Zo] = h[Wo] = h[Qo] = h[Vo] = h[sa] = h[ua] = h[la] = h[ca] = !0;
h[qo] = h[Kt] = h[ko] = !1;
function te(e, t, n, r, i, o) {
  var a, s = t & Ko, u = t & Uo, l = t & Go;
  if (n && (a = i ? n(e, r, i, o) : n(e)), a !== void 0)
    return a;
  if (!q(e))
    return e;
  var p = P(e);
  if (p) {
    if (a = oo(e), !s)
      return Dn(e, a);
  } else {
    var d = O(e), f = d == Kt || d == Yo;
    if (ie(e))
      return Hi(e, s);
    if (d == Ut || d == Dt || f && !i) {
      if (a = u || f ? {} : Io(e), !s)
        return u ? Wi(e, Bi(a, e)) : Ji(e, Gi(a, e));
    } else {
      if (!h[d])
        return i ? e : {};
      a = jo(e, d, s);
    }
  }
  o || (o = new A());
  var g = o.get(e);
  if (g)
    return g;
  o.set(e, a), Do(e) ? e.forEach(function(c) {
    a.add(te(c, t, n, c, e, o));
  }) : Lo(e) && e.forEach(function(c, v) {
    a.set(v, te(c, t, n, v, e, o));
  });
  var m = l ? u ? Nt : he : u ? xe : Q, _ = p ? void 0 : m(e);
  return Yn(_ || e, function(c, v) {
    _ && (v = c, c = e[v]), Ot(a, v, te(c, t, n, v, e, o));
  }), a;
}
var fa = "__lodash_hash_undefined__";
function pa(e) {
  return this.__data__.set(e, fa), this;
}
function ga(e) {
  return this.__data__.has(e);
}
function ae(e) {
  var t = -1, n = e == null ? 0 : e.length;
  for (this.__data__ = new I(); ++t < n; )
    this.add(e[t]);
}
ae.prototype.add = ae.prototype.push = pa;
ae.prototype.has = ga;
function da(e, t) {
  for (var n = -1, r = e == null ? 0 : e.length; ++n < r; )
    if (t(e[n], n, e))
      return !0;
  return !1;
}
function _a(e, t) {
  return e.has(t);
}
var ba = 1, ha = 2;
function Gt(e, t, n, r, i, o) {
  var a = n & ba, s = e.length, u = t.length;
  if (s != u && !(a && u > s))
    return !1;
  var l = o.get(e), p = o.get(t);
  if (l && p)
    return l == t && p == e;
  var d = -1, f = !0, g = n & ha ? new ae() : void 0;
  for (o.set(e, t), o.set(t, e); ++d < s; ) {
    var m = e[d], _ = t[d];
    if (r)
      var c = a ? r(_, m, d, t, e, o) : r(m, _, d, e, t, o);
    if (c !== void 0) {
      if (c)
        continue;
      f = !1;
      break;
    }
    if (g) {
      if (!da(t, function(v, $) {
        if (!_a(g, $) && (m === v || i(m, v, n, r, o)))
          return g.push($);
      })) {
        f = !1;
        break;
      }
    } else if (!(m === _ || i(m, _, n, r, o))) {
      f = !1;
      break;
    }
  }
  return o.delete(e), o.delete(t), f;
}
function ya(e) {
  var t = -1, n = Array(e.size);
  return e.forEach(function(r, i) {
    n[++t] = [i, r];
  }), n;
}
function ma(e) {
  var t = -1, n = Array(e.size);
  return e.forEach(function(r) {
    n[++t] = r;
  }), n;
}
var va = 1, Ta = 2, $a = "[object Boolean]", wa = "[object Date]", Oa = "[object Error]", Pa = "[object Map]", Aa = "[object Number]", Sa = "[object RegExp]", xa = "[object Set]", Ca = "[object String]", Ea = "[object Symbol]", ja = "[object ArrayBuffer]", Ia = "[object DataView]", ct = w ? w.prototype : void 0, de = ct ? ct.valueOf : void 0;
function Ma(e, t, n, r, i, o, a) {
  switch (n) {
    case Ia:
      if (e.byteLength != t.byteLength || e.byteOffset != t.byteOffset)
        return !1;
      e = e.buffer, t = t.buffer;
    case ja:
      return !(e.byteLength != t.byteLength || !o(new oe(e), new oe(t)));
    case $a:
    case wa:
    case Aa:
      return we(+e, +t);
    case Oa:
      return e.name == t.name && e.message == t.message;
    case Sa:
    case Ca:
      return e == t + "";
    case Pa:
      var s = ya;
    case xa:
      var u = r & va;
      if (s || (s = ma), e.size != t.size && !u)
        return !1;
      var l = a.get(e);
      if (l)
        return l == t;
      r |= Ta, a.set(e, t);
      var p = Gt(s(e), s(t), r, i, o, a);
      return a.delete(e), p;
    case Ea:
      if (de)
        return de.call(e) == de.call(t);
  }
  return !1;
}
var Fa = 1, La = Object.prototype, Ra = La.hasOwnProperty;
function Na(e, t, n, r, i, o) {
  var a = n & Fa, s = he(e), u = s.length, l = he(t), p = l.length;
  if (u != p && !a)
    return !1;
  for (var d = u; d--; ) {
    var f = s[d];
    if (!(a ? f in t : Ra.call(t, f)))
      return !1;
  }
  var g = o.get(e), m = o.get(t);
  if (g && m)
    return g == t && m == e;
  var _ = !0;
  o.set(e, t), o.set(t, e);
  for (var c = a; ++d < u; ) {
    f = s[d];
    var v = e[f], $ = t[f];
    if (r)
      var R = a ? r($, v, f, t, e, o) : r(v, $, f, e, t, o);
    if (!(R === void 0 ? v === $ || i(v, $, n, r, o) : R)) {
      _ = !1;
      break;
    }
    c || (c = f == "constructor");
  }
  if (_ && !c) {
    var x = e.constructor, N = t.constructor;
    x != N && "constructor" in e && "constructor" in t && !(typeof x == "function" && x instanceof x && typeof N == "function" && N instanceof N) && (_ = !1);
  }
  return o.delete(e), o.delete(t), _;
}
var Da = 1, ft = "[object Arguments]", pt = "[object Array]", ee = "[object Object]", Ka = Object.prototype, gt = Ka.hasOwnProperty;
function Ua(e, t, n, r, i, o) {
  var a = P(e), s = P(t), u = a ? pt : O(e), l = s ? pt : O(t);
  u = u == ft ? ee : u, l = l == ft ? ee : l;
  var p = u == ee, d = l == ee, f = u == l;
  if (f && ie(e)) {
    if (!ie(t))
      return !1;
    a = !0, p = !1;
  }
  if (f && !p)
    return o || (o = new A()), a || Ct(e) ? Gt(e, t, n, r, i, o) : Ma(e, t, u, n, r, i, o);
  if (!(n & Da)) {
    var g = p && gt.call(e, "__wrapped__"), m = d && gt.call(t, "__wrapped__");
    if (g || m) {
      var _ = g ? e.value() : e, c = m ? t.value() : t;
      return o || (o = new A()), i(_, c, n, r, o);
    }
  }
  return f ? (o || (o = new A()), Na(e, t, n, r, i, o)) : !1;
}
function Re(e, t, n, r, i) {
  return e === t ? !0 : e == null || t == null || !E(e) && !E(t) ? e !== e && t !== t : Ua(e, t, n, r, Re, i);
}
var Ga = 1, Ba = 2;
function za(e, t, n, r) {
  var i = n.length, o = i;
  if (e == null)
    return !o;
  for (e = Object(e); i--; ) {
    var a = n[i];
    if (a[2] ? a[1] !== e[a[0]] : !(a[0] in e))
      return !1;
  }
  for (; ++i < o; ) {
    a = n[i];
    var s = a[0], u = e[s], l = a[1];
    if (a[2]) {
      if (u === void 0 && !(s in e))
        return !1;
    } else {
      var p = new A(), d;
      if (!(d === void 0 ? Re(l, u, Ga | Ba, r, p) : d))
        return !1;
    }
  }
  return !0;
}
function Bt(e) {
  return e === e && !q(e);
}
function Ha(e) {
  for (var t = Q(e), n = t.length; n--; ) {
    var r = t[n], i = e[r];
    t[n] = [r, i, Bt(i)];
  }
  return t;
}
function zt(e, t) {
  return function(n) {
    return n == null ? !1 : n[e] === t && (t !== void 0 || e in Object(n));
  };
}
function qa(e) {
  var t = Ha(e);
  return t.length == 1 && t[0][2] ? zt(t[0][0], t[0][1]) : function(n) {
    return n === e || za(n, e, t);
  };
}
function Ya(e, t) {
  return e != null && t in Object(e);
}
function Xa(e, t, n) {
  t = ce(t, e);
  for (var r = -1, i = t.length, o = !1; ++r < i; ) {
    var a = V(t[r]);
    if (!(o = e != null && n(e, a)))
      break;
    e = e[a];
  }
  return o || ++r != i ? o : (i = e == null ? 0 : e.length, !!i && Oe(i) && wt(a, i) && (P(e) || Ae(e)));
}
function Ja(e, t) {
  return e != null && Xa(e, t, Ya);
}
var Za = 1, Wa = 2;
function Qa(e, t) {
  return Ce(e) && Bt(t) ? zt(V(e), t) : function(n) {
    var r = wi(n, e);
    return r === void 0 && r === t ? Ja(n, e) : Re(t, r, Za | Wa);
  };
}
function Va(e) {
  return function(t) {
    return t == null ? void 0 : t[e];
  };
}
function ka(e) {
  return function(t) {
    return je(t, e);
  };
}
function es(e) {
  return Ce(e) ? Va(V(e)) : ka(e);
}
function ts(e) {
  return typeof e == "function" ? e : e == null ? Tt : typeof e == "object" ? P(e) ? Qa(e[0], e[1]) : qa(e) : es(e);
}
function ns(e) {
  return function(t, n, r) {
    for (var i = -1, o = Object(t), a = r(t), s = a.length; s--; ) {
      var u = a[++i];
      if (n(o[u], u, o) === !1)
        break;
    }
    return t;
  };
}
var rs = ns();
function is(e, t) {
  return e && rs(e, t, Q);
}
function os(e) {
  var t = e == null ? 0 : e.length;
  return t ? e[t - 1] : void 0;
}
function as(e, t) {
  return t.length < 2 ? e : je(e, Fi(t, 0, -1));
}
function ss(e, t) {
  var n = {};
  return t = ts(t), is(e, function(r, i, o) {
    $e(n, t(r, i, o), r);
  }), n;
}
function us(e, t) {
  return t = ce(t, e), e = as(e, t), e == null || delete e[V(os(t))];
}
function ls(e) {
  return Mi(e) ? void 0 : e;
}
var cs = 1, fs = 2, ps = 4, Ht = Si(function(e, t) {
  var n = {};
  if (e == null)
    return n;
  var r = !1;
  t = mt(t, function(o) {
    return o = ce(o, e), r || (r = o.length > 1), o;
  }), W(e, Nt(e), n), r && (n = te(n, cs | fs | ps, ls));
  for (var i = t.length; i--; )
    us(n, t[i]);
  return n;
});
async function gs() {
  window.ms_globals || (window.ms_globals = {}), window.ms_globals.initializePromise || (window.ms_globals.initializePromise = new Promise((e) => {
    window.ms_globals.initialize = () => {
      e();
    };
  })), await window.ms_globals.initializePromise;
}
async function ds(e) {
  return await gs(), e().then((t) => t.default);
}
const qt = [
  "interactive",
  "gradio",
  "server",
  "target",
  "theme_mode",
  "root",
  "name",
  // 'visible',
  // 'elem_id',
  // 'elem_classes',
  // 'elem_style',
  "_internal",
  "props",
  // 'value',
  "_selectable",
  "loading_status",
  "value_is_output"
], _s = qt.concat(["attached_events"]);
function bs(e, t = {}, n = !1) {
  return ss(Ht(e, n ? [] : qt), (r, i) => t[i] || un(i));
}
function hs(e, t) {
  const {
    gradio: n,
    _internal: r,
    restProps: i,
    originalRestProps: o,
    ...a
  } = e, s = (i == null ? void 0 : i.attachedEvents) || [];
  return {
    ...Array.from(/* @__PURE__ */ new Set([...Object.keys(r).map((u) => {
      const l = u.match(/bind_(.+)_event/);
      return l && l[1] ? l[1] : null;
    }).filter(Boolean), ...s.map((u) => u)])).reduce((u, l) => {
      const p = l.split("_"), d = (...g) => {
        const m = g.map((c) => g && typeof c == "object" && (c.nativeEvent || c instanceof Event) ? {
          type: c.type,
          detail: c.detail,
          timestamp: c.timeStamp,
          clientX: c.clientX,
          clientY: c.clientY,
          targetId: c.target.id,
          targetClassName: c.target.className,
          altKey: c.altKey,
          ctrlKey: c.ctrlKey,
          shiftKey: c.shiftKey,
          metaKey: c.metaKey
        } : c);
        let _;
        try {
          _ = JSON.parse(JSON.stringify(m));
        } catch {
          _ = m.map((c) => c && typeof c == "object" ? Object.fromEntries(Object.entries(c).filter(([, v]) => {
            try {
              return JSON.stringify(v), !0;
            } catch {
              return !1;
            }
          })) : c);
        }
        return n.dispatch(l.replace(/[A-Z]/g, (c) => "_" + c.toLowerCase()), {
          payload: _,
          component: {
            ...a,
            ...Ht(o, _s)
          }
        });
      };
      if (p.length > 1) {
        let g = {
          ...a.props[p[0]] || (i == null ? void 0 : i[p[0]]) || {}
        };
        u[p[0]] = g;
        for (let _ = 1; _ < p.length - 1; _++) {
          const c = {
            ...a.props[p[_]] || (i == null ? void 0 : i[p[_]]) || {}
          };
          g[p[_]] = c, g = c;
        }
        const m = p[p.length - 1];
        return g[`on${m.slice(0, 1).toUpperCase()}${m.slice(1)}`] = d, u;
      }
      const f = p[0];
      return u[`on${f.slice(0, 1).toUpperCase()}${f.slice(1)}`] = d, u;
    }, {}),
    __render_eventProps: {
      props: e,
      eventsMapping: t
    }
  };
}
function ne() {
}
function ys(e, t) {
  return e != e ? t == t : e !== t || e && typeof e == "object" || typeof e == "function";
}
function ms(e, ...t) {
  if (e == null) {
    for (const r of t)
      r(void 0);
    return ne;
  }
  const n = e.subscribe(...t);
  return n.unsubscribe ? () => n.unsubscribe() : n;
}
function Yt(e) {
  let t;
  return ms(e, (n) => t = n)(), t;
}
const B = [];
function F(e, t = ne) {
  let n;
  const r = /* @__PURE__ */ new Set();
  function i(s) {
    if (ys(e, s) && (e = s, n)) {
      const u = !B.length;
      for (const l of r)
        l[1](), B.push(l, e);
      if (u) {
        for (let l = 0; l < B.length; l += 2)
          B[l][0](B[l + 1]);
        B.length = 0;
      }
    }
  }
  function o(s) {
    i(s(e));
  }
  function a(s, u = ne) {
    const l = [s, u];
    return r.add(l), r.size === 1 && (n = t(i, o) || ne), s(e), () => {
      r.delete(l), r.size === 0 && n && (n(), n = null);
    };
  }
  return {
    set: i,
    update: o,
    subscribe: a
  };
}
const {
  getContext: vs,
  setContext: ks
} = window.__gradio__svelte__internal, Ts = "$$ms-gr-loading-status-key";
function $s() {
  const e = window.ms_globals.loadingKey++, t = vs(Ts);
  return (n) => {
    if (!t || !n)
      return;
    const {
      loadingStatusMap: r,
      options: i
    } = t, {
      generating: o,
      error: a
    } = Yt(i);
    (n == null ? void 0 : n.status) === "pending" || a && (n == null ? void 0 : n.status) === "error" || (o && (n == null ? void 0 : n.status)) === "generating" ? r.update(({
      map: s
    }) => (s.set(e, n), {
      map: s
    })) : r.update(({
      map: s
    }) => (s.delete(e), {
      map: s
    }));
  };
}
const {
  getContext: fe,
  setContext: k
} = window.__gradio__svelte__internal, ws = "$$ms-gr-slots-key";
function Os() {
  const e = F({});
  return k(ws, e);
}
const Xt = "$$ms-gr-slot-params-mapping-fn-key";
function Ps() {
  return fe(Xt);
}
function As(e) {
  return k(Xt, F(e));
}
const Jt = "$$ms-gr-sub-index-context-key";
function Ss() {
  return fe(Jt) || null;
}
function dt(e) {
  return k(Jt, e);
}
function xs(e, t, n) {
  if (!Reflect.has(e, "as_item") || !Reflect.has(e, "_internal"))
    throw new Error("`as_item` and `_internal` is required");
  const r = Es(), i = Ps();
  As().set(void 0);
  const a = js({
    slot: void 0,
    index: e._internal.index,
    subIndex: e._internal.subIndex
  }), s = Ss();
  typeof s == "number" && dt(void 0);
  const u = $s();
  typeof e._internal.subIndex == "number" && dt(e._internal.subIndex), r && r.subscribe((f) => {
    a.slotKey.set(f);
  }), Cs();
  const l = e.as_item, p = (f, g) => f ? {
    ...bs({
      ...f
    }, t),
    __render_slotParamsMappingFn: i ? Yt(i) : void 0,
    __render_as_item: g,
    __render_restPropsMapping: t
  } : void 0, d = F({
    ...e,
    _internal: {
      ...e._internal,
      index: s ?? e._internal.index
    },
    restProps: p(e.restProps, l),
    originalRestProps: e.restProps
  });
  return i && i.subscribe((f) => {
    d.update((g) => ({
      ...g,
      restProps: {
        ...g.restProps,
        __slotParamsMappingFn: f
      }
    }));
  }), [d, (f) => {
    var g;
    u((g = f.restProps) == null ? void 0 : g.loading_status), d.set({
      ...f,
      _internal: {
        ...f._internal,
        index: s ?? f._internal.index
      },
      restProps: p(f.restProps, f.as_item),
      originalRestProps: f.restProps
    });
  }];
}
const Zt = "$$ms-gr-slot-key";
function Cs() {
  k(Zt, F(void 0));
}
function Es() {
  return fe(Zt);
}
const Wt = "$$ms-gr-component-slot-context-key";
function js({
  slot: e,
  index: t,
  subIndex: n
}) {
  return k(Wt, {
    slotKey: F(e),
    slotIndex: F(t),
    subSlotIndex: F(n)
  });
}
function eu() {
  return fe(Wt);
}
function Is(e) {
  return e && e.__esModule && Object.prototype.hasOwnProperty.call(e, "default") ? e.default : e;
}
var Qt = {
  exports: {}
};
/*!
	Copyright (c) 2018 Jed Watson.
	Licensed under the MIT License (MIT), see
	http://jedwatson.github.io/classnames
*/
(function(e) {
  (function() {
    var t = {}.hasOwnProperty;
    function n() {
      for (var o = "", a = 0; a < arguments.length; a++) {
        var s = arguments[a];
        s && (o = i(o, r(s)));
      }
      return o;
    }
    function r(o) {
      if (typeof o == "string" || typeof o == "number")
        return o;
      if (typeof o != "object")
        return "";
      if (Array.isArray(o))
        return n.apply(null, o);
      if (o.toString !== Object.prototype.toString && !o.toString.toString().includes("[native code]"))
        return o.toString();
      var a = "";
      for (var s in o)
        t.call(o, s) && o[s] && (a = i(a, s));
      return a;
    }
    function i(o, a) {
      return a ? o ? o + " " + a : o + a : o;
    }
    e.exports ? (n.default = n, e.exports = n) : window.classNames = n;
  })();
})(Qt);
var Ms = Qt.exports;
const Fs = /* @__PURE__ */ Is(Ms), {
  SvelteComponent: Ls,
  assign: se,
  check_outros: Vt,
  claim_component: kt,
  component_subscribe: _e,
  compute_rest_props: _t,
  create_component: en,
  create_slot: Rs,
  destroy_component: tn,
  detach: Ne,
  empty: H,
  exclude_internal_props: Ns,
  flush: M,
  get_all_dirty_from_scope: Ds,
  get_slot_changes: Ks,
  get_spread_object: nn,
  get_spread_update: rn,
  group_outros: on,
  handle_promise: Us,
  init: Gs,
  insert_hydration: De,
  mount_component: an,
  noop: T,
  safe_not_equal: Bs,
  transition_in: C,
  transition_out: L,
  update_await_block_branch: zs,
  update_slot_base: Hs
} = window.__gradio__svelte__internal;
function bt(e) {
  let t, n, r = {
    ctx: e,
    current: null,
    token: null,
    hasCatch: !1,
    pending: Ws,
    then: Ys,
    catch: qs,
    value: 20,
    blocks: [, , ,]
  };
  return Us(
    /*AwaitedBadge*/
    e[2],
    r
  ), {
    c() {
      t = H(), r.block.c();
    },
    l(i) {
      t = H(), r.block.l(i);
    },
    m(i, o) {
      De(i, t, o), r.block.m(i, r.anchor = o), r.mount = () => t.parentNode, r.anchor = t, n = !0;
    },
    p(i, o) {
      e = i, zs(r, e, o);
    },
    i(i) {
      n || (C(r.block), n = !0);
    },
    o(i) {
      for (let o = 0; o < 3; o += 1) {
        const a = r.blocks[o];
        L(a);
      }
      n = !1;
    },
    d(i) {
      i && Ne(t), r.block.d(i), r.token = null, r = null;
    }
  };
}
function qs(e) {
  return {
    c: T,
    l: T,
    m: T,
    p: T,
    i: T,
    o: T,
    d: T
  };
}
function Ys(e) {
  let t, n, r, i;
  const o = [Js, Xs], a = [];
  function s(u, l) {
    return (
      /*$mergedProps*/
      u[0]._internal.layout ? 0 : 1
    );
  }
  return t = s(e), n = a[t] = o[t](e), {
    c() {
      n.c(), r = H();
    },
    l(u) {
      n.l(u), r = H();
    },
    m(u, l) {
      a[t].m(u, l), De(u, r, l), i = !0;
    },
    p(u, l) {
      let p = t;
      t = s(u), t === p ? a[t].p(u, l) : (on(), L(a[p], 1, 1, () => {
        a[p] = null;
      }), Vt(), n = a[t], n ? n.p(u, l) : (n = a[t] = o[t](u), n.c()), C(n, 1), n.m(r.parentNode, r));
    },
    i(u) {
      i || (C(n), i = !0);
    },
    o(u) {
      L(n), i = !1;
    },
    d(u) {
      u && Ne(r), a[t].d(u);
    }
  };
}
function Xs(e) {
  let t, n;
  const r = [
    /*badge_props*/
    e[1]
  ];
  let i = {};
  for (let o = 0; o < r.length; o += 1)
    i = se(i, r[o]);
  return t = new /*Badge*/
  e[20]({
    props: i
  }), {
    c() {
      en(t.$$.fragment);
    },
    l(o) {
      kt(t.$$.fragment, o);
    },
    m(o, a) {
      an(t, o, a), n = !0;
    },
    p(o, a) {
      const s = a & /*badge_props*/
      2 ? rn(r, [nn(
        /*badge_props*/
        o[1]
      )]) : {};
      t.$set(s);
    },
    i(o) {
      n || (C(t.$$.fragment, o), n = !0);
    },
    o(o) {
      L(t.$$.fragment, o), n = !1;
    },
    d(o) {
      tn(t, o);
    }
  };
}
function Js(e) {
  let t, n;
  const r = [
    /*badge_props*/
    e[1]
  ];
  let i = {
    $$slots: {
      default: [Zs]
    },
    $$scope: {
      ctx: e
    }
  };
  for (let o = 0; o < r.length; o += 1)
    i = se(i, r[o]);
  return t = new /*Badge*/
  e[20]({
    props: i
  }), {
    c() {
      en(t.$$.fragment);
    },
    l(o) {
      kt(t.$$.fragment, o);
    },
    m(o, a) {
      an(t, o, a), n = !0;
    },
    p(o, a) {
      const s = a & /*badge_props*/
      2 ? rn(r, [nn(
        /*badge_props*/
        o[1]
      )]) : {};
      a & /*$$scope*/
      131072 && (s.$$scope = {
        dirty: a,
        ctx: o
      }), t.$set(s);
    },
    i(o) {
      n || (C(t.$$.fragment, o), n = !0);
    },
    o(o) {
      L(t.$$.fragment, o), n = !1;
    },
    d(o) {
      tn(t, o);
    }
  };
}
function Zs(e) {
  let t;
  const n = (
    /*#slots*/
    e[16].default
  ), r = Rs(
    n,
    e,
    /*$$scope*/
    e[17],
    null
  );
  return {
    c() {
      r && r.c();
    },
    l(i) {
      r && r.l(i);
    },
    m(i, o) {
      r && r.m(i, o), t = !0;
    },
    p(i, o) {
      r && r.p && (!t || o & /*$$scope*/
      131072) && Hs(
        r,
        n,
        i,
        /*$$scope*/
        i[17],
        t ? Ks(
          n,
          /*$$scope*/
          i[17],
          o,
          null
        ) : Ds(
          /*$$scope*/
          i[17]
        ),
        null
      );
    },
    i(i) {
      t || (C(r, i), t = !0);
    },
    o(i) {
      L(r, i), t = !1;
    },
    d(i) {
      r && r.d(i);
    }
  };
}
function Ws(e) {
  return {
    c: T,
    l: T,
    m: T,
    p: T,
    i: T,
    o: T,
    d: T
  };
}
function Qs(e) {
  let t, n, r = (
    /*$mergedProps*/
    e[0].visible && bt(e)
  );
  return {
    c() {
      r && r.c(), t = H();
    },
    l(i) {
      r && r.l(i), t = H();
    },
    m(i, o) {
      r && r.m(i, o), De(i, t, o), n = !0;
    },
    p(i, [o]) {
      /*$mergedProps*/
      i[0].visible ? r ? (r.p(i, o), o & /*$mergedProps*/
      1 && C(r, 1)) : (r = bt(i), r.c(), C(r, 1), r.m(t.parentNode, t)) : r && (on(), L(r, 1, 1, () => {
        r = null;
      }), Vt());
    },
    i(i) {
      n || (C(r), n = !0);
    },
    o(i) {
      L(r), n = !1;
    },
    d(i) {
      i && Ne(t), r && r.d(i);
    }
  };
}
function Vs(e, t, n) {
  let r;
  const i = ["gradio", "props", "_internal", "as_item", "visible", "elem_id", "elem_classes", "elem_style"];
  let o = _t(t, i), a, s, u, {
    $$slots: l = {},
    $$scope: p
  } = t;
  const d = ds(() => import("./badge-DR1_TiLi.js"));
  let {
    gradio: f
  } = t, {
    props: g = {}
  } = t;
  const m = F(g);
  _e(e, m, (b) => n(15, u = b));
  let {
    _internal: _ = {}
  } = t, {
    as_item: c
  } = t, {
    visible: v = !0
  } = t, {
    elem_id: $ = ""
  } = t, {
    elem_classes: R = []
  } = t, {
    elem_style: x = {}
  } = t;
  const [N, sn] = xs({
    gradio: f,
    props: u,
    _internal: _,
    visible: v,
    elem_id: $,
    elem_classes: R,
    elem_style: x,
    as_item: c,
    restProps: o
  });
  _e(e, N, (b) => n(0, s = b));
  const Ke = Os();
  return _e(e, Ke, (b) => n(14, a = b)), e.$$set = (b) => {
    t = se(se({}, t), Ns(b)), n(19, o = _t(t, i)), "gradio" in b && n(6, f = b.gradio), "props" in b && n(7, g = b.props), "_internal" in b && n(8, _ = b._internal), "as_item" in b && n(9, c = b.as_item), "visible" in b && n(10, v = b.visible), "elem_id" in b && n(11, $ = b.elem_id), "elem_classes" in b && n(12, R = b.elem_classes), "elem_style" in b && n(13, x = b.elem_style), "$$scope" in b && n(17, p = b.$$scope);
  }, e.$$.update = () => {
    e.$$.dirty & /*props*/
    128 && m.update((b) => ({
      ...b,
      ...g
    })), sn({
      gradio: f,
      props: u,
      _internal: _,
      visible: v,
      elem_id: $,
      elem_classes: R,
      elem_style: x,
      as_item: c,
      restProps: o
    }), e.$$.dirty & /*$mergedProps, $slots*/
    16385 && n(1, r = {
      style: s.elem_style,
      className: Fs(s.elem_classes, "ms-gr-antd-badge"),
      id: s.elem_id,
      ...s.restProps,
      ...s.props,
      ...hs(s),
      slots: a
    });
  }, [s, r, d, m, N, Ke, f, g, _, c, v, $, R, x, a, u, l, p];
}
class tu extends Ls {
  constructor(t) {
    super(), Gs(this, t, Vs, Qs, Bs, {
      gradio: 6,
      props: 7,
      _internal: 8,
      as_item: 9,
      visible: 10,
      elem_id: 11,
      elem_classes: 12,
      elem_style: 13
    });
  }
  get gradio() {
    return this.$$.ctx[6];
  }
  set gradio(t) {
    this.$$set({
      gradio: t
    }), M();
  }
  get props() {
    return this.$$.ctx[7];
  }
  set props(t) {
    this.$$set({
      props: t
    }), M();
  }
  get _internal() {
    return this.$$.ctx[8];
  }
  set _internal(t) {
    this.$$set({
      _internal: t
    }), M();
  }
  get as_item() {
    return this.$$.ctx[9];
  }
  set as_item(t) {
    this.$$set({
      as_item: t
    }), M();
  }
  get visible() {
    return this.$$.ctx[10];
  }
  set visible(t) {
    this.$$set({
      visible: t
    }), M();
  }
  get elem_id() {
    return this.$$.ctx[11];
  }
  set elem_id(t) {
    this.$$set({
      elem_id: t
    }), M();
  }
  get elem_classes() {
    return this.$$.ctx[12];
  }
  set elem_classes(t) {
    this.$$set({
      elem_classes: t
    }), M();
  }
  get elem_style() {
    return this.$$.ctx[13];
  }
  set elem_style(t) {
    this.$$set({
      elem_style: t
    }), M();
  }
}
export {
  tu as I,
  q as a,
  eu as g,
  Te as i,
  S as r,
  F as w
};
