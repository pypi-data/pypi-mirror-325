import { g as Qt, w as M } from "./XProvider-BCUhPu_l.js";
import { a as Vt, b as et, r as $t, c as te } from "./Index-CDkcF4bD.js";
const x = window.ms_globals.React, qt = window.ms_globals.React.forwardRef, Yt = window.ms_globals.React.useRef, zt = window.ms_globals.React.useState, Tt = window.ms_globals.React.useEffect, Jt = window.ms_globals.React.useMemo, tt = window.ms_globals.ReactDOM.createPortal, Xt = window.ms_globals.internalContext.useContextPropsContext, mt = window.ms_globals.internalContext.ContextPropsProvider, ee = window.ms_globals.antdCssinjs.StyleProvider, ht = window.ms_globals.antd.theme, ne = window.ms_globals.antd.ConfigProvider, re = window.ms_globals.dayjs;
var ie = /\s/;
function ae(e) {
  for (var t = e.length; t-- && ie.test(e.charAt(t)); )
    ;
  return t;
}
var oe = /^\s+/;
function se(e) {
  return e && e.slice(0, ae(e) + 1).replace(oe, "");
}
var pt = NaN, le = /^[-+]0x[0-9a-f]+$/i, ce = /^0b[01]+$/i, ue = /^0o[0-7]+$/i, de = parseInt;
function yt(e) {
  if (typeof e == "number")
    return e;
  if (Vt(e))
    return pt;
  if (et(e)) {
    var t = typeof e.valueOf == "function" ? e.valueOf() : e;
    e = et(t) ? t + "" : t;
  }
  if (typeof e != "string")
    return e === 0 ? e : +e;
  e = se(e);
  var n = ce.test(e);
  return n || ue.test(e) ? de(e.slice(2), n ? 2 : 8) : le.test(e) ? pt : +e;
}
var J = function() {
  return $t.Date.now();
}, fe = "Expected a function", me = Math.max, he = Math.min;
function pe(e, t, n) {
  var r, i, a, o, s, l, h = 0, p = !1, c = !1, _ = !0;
  if (typeof e != "function")
    throw new TypeError(fe);
  t = yt(t) || 0, et(n) && (p = !!n.leading, c = "maxWait" in n, a = c ? me(yt(n.maxWait) || 0, t) : a, _ = "trailing" in n ? !!n.trailing : _);
  function m(f) {
    var C = r, F = i;
    return r = i = void 0, h = f, o = e.apply(F, C), o;
  }
  function k(f) {
    return h = f, s = setTimeout(w, t), p ? m(f) : o;
  }
  function d(f) {
    var C = f - l, F = f - h, ft = t - C;
    return c ? he(ft, a - F) : ft;
  }
  function y(f) {
    var C = f - l, F = f - h;
    return l === void 0 || C >= t || C < 0 || c && F >= a;
  }
  function w() {
    var f = J();
    if (y(f))
      return E(f);
    s = setTimeout(w, d(f));
  }
  function E(f) {
    return s = void 0, _ && r ? m(f) : (r = i = void 0, o);
  }
  function v() {
    s !== void 0 && clearTimeout(s), h = 0, r = l = i = s = void 0;
  }
  function u() {
    return s === void 0 ? o : E(J());
  }
  function b() {
    var f = J(), C = y(f);
    if (r = arguments, i = this, l = f, C) {
      if (s === void 0)
        return k(l);
      if (c)
        return clearTimeout(s), s = setTimeout(w, t), m(l);
    }
    return s === void 0 && (s = setTimeout(w, t)), o;
  }
  return b.cancel = v, b.flush = u, b;
}
var At = {
  exports: {}
}, G = {};
/**
 * @license React
 * react-jsx-runtime.production.min.js
 *
 * Copyright (c) Facebook, Inc. and its affiliates.
 *
 * This source code is licensed under the MIT license found in the
 * LICENSE file in the root directory of this source tree.
 */
var ye = x, _e = Symbol.for("react.element"), we = Symbol.for("react.fragment"), Pe = Object.prototype.hasOwnProperty, ge = ye.__SECRET_INTERNALS_DO_NOT_USE_OR_YOU_WILL_BE_FIRED.ReactCurrentOwner, be = {
  key: !0,
  ref: !0,
  __self: !0,
  __source: !0
};
function Ft(e, t, n) {
  var r, i = {}, a = null, o = null;
  n !== void 0 && (a = "" + n), t.key !== void 0 && (a = "" + t.key), t.ref !== void 0 && (o = t.ref);
  for (r in t) Pe.call(t, r) && !be.hasOwnProperty(r) && (i[r] = t[r]);
  if (e && e.defaultProps) for (r in t = e.defaultProps, t) i[r] === void 0 && (i[r] = t[r]);
  return {
    $$typeof: _e,
    type: e,
    key: a,
    ref: o,
    props: i,
    _owner: ge.current
  };
}
G.Fragment = we;
G.jsx = Ft;
G.jsxs = Ft;
At.exports = G;
var I = At.exports;
const {
  SvelteComponent: je,
  assign: _t,
  binding_callbacks: wt,
  check_outros: ke,
  children: Nt,
  claim_element: Dt,
  claim_space: Ee,
  component_subscribe: Pt,
  compute_slots: ve,
  create_slot: Ce,
  detach: z,
  element: Mt,
  empty: gt,
  exclude_internal_props: bt,
  get_all_dirty_from_scope: Se,
  get_slot_changes: xe,
  group_outros: Ie,
  init: Oe,
  insert_hydration: L,
  safe_not_equal: Re,
  set_custom_element_data: Lt,
  space: ze,
  transition_in: W,
  transition_out: nt,
  update_slot_base: Te
} = window.__gradio__svelte__internal, {
  beforeUpdate: Ae,
  getContext: Fe,
  onDestroy: Ne,
  setContext: De
} = window.__gradio__svelte__internal;
function jt(e) {
  let t, n;
  const r = (
    /*#slots*/
    e[7].default
  ), i = Ce(
    r,
    e,
    /*$$scope*/
    e[6],
    null
  );
  return {
    c() {
      t = Mt("svelte-slot"), i && i.c(), this.h();
    },
    l(a) {
      t = Dt(a, "SVELTE-SLOT", {
        class: !0
      });
      var o = Nt(t);
      i && i.l(o), o.forEach(z), this.h();
    },
    h() {
      Lt(t, "class", "svelte-1rt0kpf");
    },
    m(a, o) {
      L(a, t, o), i && i.m(t, null), e[9](t), n = !0;
    },
    p(a, o) {
      i && i.p && (!n || o & /*$$scope*/
      64) && Te(
        i,
        r,
        a,
        /*$$scope*/
        a[6],
        n ? xe(
          r,
          /*$$scope*/
          a[6],
          o,
          null
        ) : Se(
          /*$$scope*/
          a[6]
        ),
        null
      );
    },
    i(a) {
      n || (W(i, a), n = !0);
    },
    o(a) {
      nt(i, a), n = !1;
    },
    d(a) {
      a && z(t), i && i.d(a), e[9](null);
    }
  };
}
function Me(e) {
  let t, n, r, i, a = (
    /*$$slots*/
    e[4].default && jt(e)
  );
  return {
    c() {
      t = Mt("react-portal-target"), n = ze(), a && a.c(), r = gt(), this.h();
    },
    l(o) {
      t = Dt(o, "REACT-PORTAL-TARGET", {
        class: !0
      }), Nt(t).forEach(z), n = Ee(o), a && a.l(o), r = gt(), this.h();
    },
    h() {
      Lt(t, "class", "svelte-1rt0kpf");
    },
    m(o, s) {
      L(o, t, s), e[8](t), L(o, n, s), a && a.m(o, s), L(o, r, s), i = !0;
    },
    p(o, [s]) {
      /*$$slots*/
      o[4].default ? a ? (a.p(o, s), s & /*$$slots*/
      16 && W(a, 1)) : (a = jt(o), a.c(), W(a, 1), a.m(r.parentNode, r)) : a && (Ie(), nt(a, 1, 1, () => {
        a = null;
      }), ke());
    },
    i(o) {
      i || (W(a), i = !0);
    },
    o(o) {
      nt(a), i = !1;
    },
    d(o) {
      o && (z(t), z(n), z(r)), e[8](null), a && a.d(o);
    }
  };
}
function kt(e) {
  const {
    svelteInit: t,
    ...n
  } = e;
  return n;
}
function Le(e, t, n) {
  let r, i, {
    $$slots: a = {},
    $$scope: o
  } = t;
  const s = ve(a);
  let {
    svelteInit: l
  } = t;
  const h = M(kt(t)), p = M();
  Pt(e, p, (u) => n(0, r = u));
  const c = M();
  Pt(e, c, (u) => n(1, i = u));
  const _ = [], m = Fe("$$ms-gr-react-wrapper"), {
    slotKey: k,
    slotIndex: d,
    subSlotIndex: y
  } = Qt() || {}, w = l({
    parent: m,
    props: h,
    target: p,
    slot: c,
    slotKey: k,
    slotIndex: d,
    subSlotIndex: y,
    onDestroy(u) {
      _.push(u);
    }
  });
  De("$$ms-gr-react-wrapper", w), Ae(() => {
    h.set(kt(t));
  }), Ne(() => {
    _.forEach((u) => u());
  });
  function E(u) {
    wt[u ? "unshift" : "push"](() => {
      r = u, p.set(r);
    });
  }
  function v(u) {
    wt[u ? "unshift" : "push"](() => {
      i = u, c.set(i);
    });
  }
  return e.$$set = (u) => {
    n(17, t = _t(_t({}, t), bt(u))), "svelteInit" in u && n(5, l = u.svelteInit), "$$scope" in u && n(6, o = u.$$scope);
  }, t = bt(t), [r, i, p, c, s, l, o, a, E, v];
}
class We extends je {
  constructor(t) {
    super(), Oe(this, t, Le, Me, Re, {
      svelteInit: 5
    });
  }
}
const Et = window.ms_globals.rerender, Q = window.ms_globals.tree;
function Ke(e, t = {}) {
  function n(r) {
    const i = M(), a = new We({
      ...r,
      props: {
        svelteInit(o) {
          window.ms_globals.autokey += 1;
          const s = {
            key: window.ms_globals.autokey,
            svelteInstance: i,
            reactComponent: e,
            props: o.props,
            slot: o.slot,
            target: o.target,
            slotIndex: o.slotIndex,
            subSlotIndex: o.subSlotIndex,
            ignore: t.ignore,
            slotKey: o.slotKey,
            nodes: []
          }, l = o.parent ?? Q;
          return l.nodes = [...l.nodes, s], Et({
            createPortal: tt,
            node: Q
          }), o.onDestroy(() => {
            l.nodes = l.nodes.filter((h) => h.svelteInstance !== i), Et({
              createPortal: tt,
              node: Q
            });
          }), s;
        },
        ...r.props
      }
    });
    return i.set(a), a;
  }
  return new Promise((r) => {
    window.ms_globals.initializePromise.then(() => {
      r(n);
    });
  });
}
const Ue = ["animationIterationCount", "borderImageOutset", "borderImageSlice", "borderImageWidth", "boxFlex", "boxFlexGroup", "boxOrdinalGroup", "columnCount", "columns", "flex", "flexGrow", "flexPositive", "flexShrink", "flexNegative", "flexOrder", "gridArea", "gridColumn", "gridColumnEnd", "gridColumnStart", "gridRow", "gridRowEnd", "gridRowStart", "lineClamp", "lineHeight", "opacity", "order", "orphans", "tabSize", "widows", "zIndex", "zoom", "fontWeight", "letterSpacing", "lineHeight"];
function Be(e) {
  return e ? Object.keys(e).reduce((t, n) => {
    const r = e[n];
    return t[n] = Ge(n, r), t;
  }, {}) : {};
}
function Ge(e, t) {
  return typeof t == "number" && !Ue.includes(e) ? t + "px" : t;
}
function rt(e) {
  const t = [], n = e.cloneNode(!1);
  if (e._reactElement) {
    const i = x.Children.toArray(e._reactElement.props.children).map((a) => {
      if (x.isValidElement(a) && a.props.__slot__) {
        const {
          portals: o,
          clonedElement: s
        } = rt(a.props.el);
        return x.cloneElement(a, {
          ...a.props,
          el: s,
          children: [...x.Children.toArray(a.props.children), ...o]
        });
      }
      return null;
    });
    return i.originalChildren = e._reactElement.props.children, t.push(tt(x.cloneElement(e._reactElement, {
      ...e._reactElement.props,
      children: i
    }), n)), {
      clonedElement: n,
      portals: t
    };
  }
  Object.keys(e.getEventListeners()).forEach((i) => {
    e.getEventListeners(i).forEach(({
      listener: o,
      type: s,
      useCapture: l
    }) => {
      n.addEventListener(s, o, l);
    });
  });
  const r = Array.from(e.childNodes);
  for (let i = 0; i < r.length; i++) {
    const a = r[i];
    if (a.nodeType === 1) {
      const {
        clonedElement: o,
        portals: s
      } = rt(a);
      t.push(...s), n.appendChild(o);
    } else a.nodeType === 3 && n.appendChild(a.cloneNode());
  }
  return {
    clonedElement: n,
    portals: t
  };
}
function He(e, t) {
  e && (typeof e == "function" ? e(t) : e.current = t);
}
const Wt = qt(({
  slot: e,
  clone: t,
  className: n,
  style: r,
  observeAttributes: i
}, a) => {
  const o = Yt(), [s, l] = zt([]), {
    forceClone: h
  } = Xt(), p = h ? !0 : t;
  return Tt(() => {
    var k;
    if (!o.current || !e)
      return;
    let c = e;
    function _() {
      let d = c;
      if (c.tagName.toLowerCase() === "svelte-slot" && c.children.length === 1 && c.children[0] && (d = c.children[0], d.tagName.toLowerCase() === "react-portal-target" && d.children[0] && (d = d.children[0])), He(a, d), n && d.classList.add(...n.split(" ")), r) {
        const y = Be(r);
        Object.keys(y).forEach((w) => {
          d.style[w] = y[w];
        });
      }
    }
    let m = null;
    if (p && window.MutationObserver) {
      let d = function() {
        var v, u, b;
        (v = o.current) != null && v.contains(c) && ((u = o.current) == null || u.removeChild(c));
        const {
          portals: w,
          clonedElement: E
        } = rt(e);
        c = E, l(w), c.style.display = "contents", _(), (b = o.current) == null || b.appendChild(c);
      };
      d();
      const y = pe(() => {
        d(), m == null || m.disconnect(), m == null || m.observe(e, {
          childList: !0,
          subtree: !0,
          attributes: i
        });
      }, 50);
      m = new window.MutationObserver(y), m.observe(e, {
        attributes: !0,
        childList: !0,
        subtree: !0
      });
    } else
      c.style.display = "contents", _(), (k = o.current) == null || k.appendChild(c);
    return () => {
      var d, y;
      c.style.display = "", (d = o.current) != null && d.contains(c) && ((y = o.current) == null || y.removeChild(c)), m == null || m.disconnect();
    };
  }, [e, p, n, r, a, i]), x.createElement("react-child", {
    ref: o,
    style: {
      display: "contents"
    }
  }, ...s);
});
function Ze(e) {
  return /^(?:async\s+)?(?:function\s*(?:\w*\s*)?\(|\([\w\s,=]*\)\s*=>|\(\{[\w\s,=]*\}\)\s*=>|function\s*\*\s*\w*\s*\()/i.test(e.trim());
}
function qe(e, t = !1) {
  try {
    if (te(e))
      return e;
    if (t && !Ze(e))
      return;
    if (typeof e == "string") {
      let n = e.trim();
      return n.startsWith(";") && (n = n.slice(1)), n.endsWith(";") && (n = n.slice(0, -1)), new Function(`return (...args) => (${n})(...args)`)();
    }
    return;
  } catch {
    return;
  }
}
function X(e, t) {
  return Jt(() => qe(e, t), [e, t]);
}
function vt(e, t) {
  return e ? /* @__PURE__ */ I.jsx(Wt, {
    slot: e,
    clone: t == null ? void 0 : t.clone
  }) : null;
}
function Ye({
  key: e,
  slots: t,
  targets: n
}, r) {
  return t[e] ? (...i) => n ? n.map((a, o) => /* @__PURE__ */ I.jsx(mt, {
    params: i,
    forceClone: !0,
    children: vt(a, {
      clone: !0,
      ...r
    })
  }, o)) : /* @__PURE__ */ I.jsx(mt, {
    params: i,
    forceClone: !0,
    children: vt(t[e], {
      clone: !0,
      ...r
    })
  }) : void 0;
}
var Kt = Symbol.for("immer-nothing"), Ct = Symbol.for("immer-draftable"), P = Symbol.for("immer-state");
function j(e, ...t) {
  throw new Error(`[Immer] minified error nr: ${e}. Full error at: https://bit.ly/3cXEKWf`);
}
var T = Object.getPrototypeOf;
function A(e) {
  return !!e && !!e[P];
}
function O(e) {
  var t;
  return e ? Ut(e) || Array.isArray(e) || !!e[Ct] || !!((t = e.constructor) != null && t[Ct]) || Z(e) || q(e) : !1;
}
var Je = Object.prototype.constructor.toString();
function Ut(e) {
  if (!e || typeof e != "object") return !1;
  const t = T(e);
  if (t === null)
    return !0;
  const n = Object.hasOwnProperty.call(t, "constructor") && t.constructor;
  return n === Object ? !0 : typeof n == "function" && Function.toString.call(n) === Je;
}
function K(e, t) {
  H(e) === 0 ? Reflect.ownKeys(e).forEach((n) => {
    t(n, e[n], e);
  }) : e.forEach((n, r) => t(r, n, e));
}
function H(e) {
  const t = e[P];
  return t ? t.type_ : Array.isArray(e) ? 1 : Z(e) ? 2 : q(e) ? 3 : 0;
}
function it(e, t) {
  return H(e) === 2 ? e.has(t) : Object.prototype.hasOwnProperty.call(e, t);
}
function Bt(e, t, n) {
  const r = H(e);
  r === 2 ? e.set(t, n) : r === 3 ? e.add(n) : e[t] = n;
}
function Qe(e, t) {
  return e === t ? e !== 0 || 1 / e === 1 / t : e !== e && t !== t;
}
function Z(e) {
  return e instanceof Map;
}
function q(e) {
  return e instanceof Set;
}
function S(e) {
  return e.copy_ || e.base_;
}
function at(e, t) {
  if (Z(e))
    return new Map(e);
  if (q(e))
    return new Set(e);
  if (Array.isArray(e)) return Array.prototype.slice.call(e);
  const n = Ut(e);
  if (t === !0 || t === "class_only" && !n) {
    const r = Object.getOwnPropertyDescriptors(e);
    delete r[P];
    let i = Reflect.ownKeys(r);
    for (let a = 0; a < i.length; a++) {
      const o = i[a], s = r[o];
      s.writable === !1 && (s.writable = !0, s.configurable = !0), (s.get || s.set) && (r[o] = {
        configurable: !0,
        writable: !0,
        // could live with !!desc.set as well here...
        enumerable: s.enumerable,
        value: e[o]
      });
    }
    return Object.create(T(e), r);
  } else {
    const r = T(e);
    if (r !== null && n)
      return {
        ...e
      };
    const i = Object.create(r);
    return Object.assign(i, e);
  }
}
function ut(e, t = !1) {
  return Y(e) || A(e) || !O(e) || (H(e) > 1 && (e.set = e.add = e.clear = e.delete = Xe), Object.freeze(e), t && Object.entries(e).forEach(([n, r]) => ut(r, !0))), e;
}
function Xe() {
  j(2);
}
function Y(e) {
  return Object.isFrozen(e);
}
var Ve = {};
function R(e) {
  const t = Ve[e];
  return t || j(0, e), t;
}
var N;
function Gt() {
  return N;
}
function $e(e, t) {
  return {
    drafts_: [],
    parent_: e,
    immer_: t,
    // Whenever the modified draft contains a draft from another scope, we
    // need to prevent auto-freezing so the unowned draft can be finalized.
    canAutoFreeze_: !0,
    unfinalizedDrafts_: 0
  };
}
function St(e, t) {
  t && (R("Patches"), e.patches_ = [], e.inversePatches_ = [], e.patchListener_ = t);
}
function ot(e) {
  st(e), e.drafts_.forEach(tn), e.drafts_ = null;
}
function st(e) {
  e === N && (N = e.parent_);
}
function xt(e) {
  return N = $e(N, e);
}
function tn(e) {
  const t = e[P];
  t.type_ === 0 || t.type_ === 1 ? t.revoke_() : t.revoked_ = !0;
}
function It(e, t) {
  t.unfinalizedDrafts_ = t.drafts_.length;
  const n = t.drafts_[0];
  return e !== void 0 && e !== n ? (n[P].modified_ && (ot(t), j(4)), O(e) && (e = U(t, e), t.parent_ || B(t, e)), t.patches_ && R("Patches").generateReplacementPatches_(n[P].base_, e, t.patches_, t.inversePatches_)) : e = U(t, n, []), ot(t), t.patches_ && t.patchListener_(t.patches_, t.inversePatches_), e !== Kt ? e : void 0;
}
function U(e, t, n) {
  if (Y(t)) return t;
  const r = t[P];
  if (!r)
    return K(t, (i, a) => Ot(e, r, t, i, a, n)), t;
  if (r.scope_ !== e) return t;
  if (!r.modified_)
    return B(e, r.base_, !0), r.base_;
  if (!r.finalized_) {
    r.finalized_ = !0, r.scope_.unfinalizedDrafts_--;
    const i = r.copy_;
    let a = i, o = !1;
    r.type_ === 3 && (a = new Set(i), i.clear(), o = !0), K(a, (s, l) => Ot(e, r, i, s, l, n, o)), B(e, i, !1), n && e.patches_ && R("Patches").generatePatches_(r, n, e.patches_, e.inversePatches_);
  }
  return r.copy_;
}
function Ot(e, t, n, r, i, a, o) {
  if (A(i)) {
    const s = a && t && t.type_ !== 3 && // Set objects are atomic since they have no keys.
    !it(t.assigned_, r) ? a.concat(r) : void 0, l = U(e, i, s);
    if (Bt(n, r, l), A(l))
      e.canAutoFreeze_ = !1;
    else return;
  } else o && n.add(i);
  if (O(i) && !Y(i)) {
    if (!e.immer_.autoFreeze_ && e.unfinalizedDrafts_ < 1)
      return;
    U(e, i), (!t || !t.scope_.parent_) && typeof r != "symbol" && Object.prototype.propertyIsEnumerable.call(n, r) && B(e, i);
  }
}
function B(e, t, n = !1) {
  !e.parent_ && e.immer_.autoFreeze_ && e.canAutoFreeze_ && ut(t, n);
}
function en(e, t) {
  const n = Array.isArray(e), r = {
    type_: n ? 1 : 0,
    // Track which produce call this is associated with.
    scope_: t ? t.scope_ : Gt(),
    // True for both shallow and deep changes.
    modified_: !1,
    // Used during finalization.
    finalized_: !1,
    // Track which properties have been assigned (true) or deleted (false).
    assigned_: {},
    // The parent draft state.
    parent_: t,
    // The base state.
    base_: e,
    // The base proxy.
    draft_: null,
    // set below
    // The base copy with any updated values.
    copy_: null,
    // Called by the `produce` function.
    revoke_: null,
    isManual_: !1
  };
  let i = r, a = dt;
  n && (i = [r], a = D);
  const {
    revoke: o,
    proxy: s
  } = Proxy.revocable(i, a);
  return r.draft_ = s, r.revoke_ = o, s;
}
var dt = {
  get(e, t) {
    if (t === P) return e;
    const n = S(e);
    if (!it(n, t))
      return nn(e, n, t);
    const r = n[t];
    return e.finalized_ || !O(r) ? r : r === V(e.base_, t) ? ($(e), e.copy_[t] = ct(r, e)) : r;
  },
  has(e, t) {
    return t in S(e);
  },
  ownKeys(e) {
    return Reflect.ownKeys(S(e));
  },
  set(e, t, n) {
    const r = Ht(S(e), t);
    if (r != null && r.set)
      return r.set.call(e.draft_, n), !0;
    if (!e.modified_) {
      const i = V(S(e), t), a = i == null ? void 0 : i[P];
      if (a && a.base_ === n)
        return e.copy_[t] = n, e.assigned_[t] = !1, !0;
      if (Qe(n, i) && (n !== void 0 || it(e.base_, t))) return !0;
      $(e), lt(e);
    }
    return e.copy_[t] === n && // special case: handle new props with value 'undefined'
    (n !== void 0 || t in e.copy_) || // special case: NaN
    Number.isNaN(n) && Number.isNaN(e.copy_[t]) || (e.copy_[t] = n, e.assigned_[t] = !0), !0;
  },
  deleteProperty(e, t) {
    return V(e.base_, t) !== void 0 || t in e.base_ ? (e.assigned_[t] = !1, $(e), lt(e)) : delete e.assigned_[t], e.copy_ && delete e.copy_[t], !0;
  },
  // Note: We never coerce `desc.value` into an Immer draft, because we can't make
  // the same guarantee in ES5 mode.
  getOwnPropertyDescriptor(e, t) {
    const n = S(e), r = Reflect.getOwnPropertyDescriptor(n, t);
    return r && {
      writable: !0,
      configurable: e.type_ !== 1 || t !== "length",
      enumerable: r.enumerable,
      value: n[t]
    };
  },
  defineProperty() {
    j(11);
  },
  getPrototypeOf(e) {
    return T(e.base_);
  },
  setPrototypeOf() {
    j(12);
  }
}, D = {};
K(dt, (e, t) => {
  D[e] = function() {
    return arguments[0] = arguments[0][0], t.apply(this, arguments);
  };
});
D.deleteProperty = function(e, t) {
  return D.set.call(this, e, t, void 0);
};
D.set = function(e, t, n) {
  return dt.set.call(this, e[0], t, n, e[0]);
};
function V(e, t) {
  const n = e[P];
  return (n ? S(n) : e)[t];
}
function nn(e, t, n) {
  var i;
  const r = Ht(t, n);
  return r ? "value" in r ? r.value : (
    // This is a very special case, if the prop is a getter defined by the
    // prototype, we should invoke it with the draft as context!
    (i = r.get) == null ? void 0 : i.call(e.draft_)
  ) : void 0;
}
function Ht(e, t) {
  if (!(t in e)) return;
  let n = T(e);
  for (; n; ) {
    const r = Object.getOwnPropertyDescriptor(n, t);
    if (r) return r;
    n = T(n);
  }
}
function lt(e) {
  e.modified_ || (e.modified_ = !0, e.parent_ && lt(e.parent_));
}
function $(e) {
  e.copy_ || (e.copy_ = at(e.base_, e.scope_.immer_.useStrictShallowCopy_));
}
var rn = class {
  constructor(e) {
    this.autoFreeze_ = !0, this.useStrictShallowCopy_ = !1, this.produce = (t, n, r) => {
      if (typeof t == "function" && typeof n != "function") {
        const a = n;
        n = t;
        const o = this;
        return function(l = a, ...h) {
          return o.produce(l, (p) => n.call(this, p, ...h));
        };
      }
      typeof n != "function" && j(6), r !== void 0 && typeof r != "function" && j(7);
      let i;
      if (O(t)) {
        const a = xt(this), o = ct(t, void 0);
        let s = !0;
        try {
          i = n(o), s = !1;
        } finally {
          s ? ot(a) : st(a);
        }
        return St(a, r), It(i, a);
      } else if (!t || typeof t != "object") {
        if (i = n(t), i === void 0 && (i = t), i === Kt && (i = void 0), this.autoFreeze_ && ut(i, !0), r) {
          const a = [], o = [];
          R("Patches").generateReplacementPatches_(t, i, a, o), r(a, o);
        }
        return i;
      } else j(1, t);
    }, this.produceWithPatches = (t, n) => {
      if (typeof t == "function")
        return (o, ...s) => this.produceWithPatches(o, (l) => t(l, ...s));
      let r, i;
      return [this.produce(t, n, (o, s) => {
        r = o, i = s;
      }), r, i];
    }, typeof (e == null ? void 0 : e.autoFreeze) == "boolean" && this.setAutoFreeze(e.autoFreeze), typeof (e == null ? void 0 : e.useStrictShallowCopy) == "boolean" && this.setUseStrictShallowCopy(e.useStrictShallowCopy);
  }
  createDraft(e) {
    O(e) || j(8), A(e) && (e = an(e));
    const t = xt(this), n = ct(e, void 0);
    return n[P].isManual_ = !0, st(t), n;
  }
  finishDraft(e, t) {
    const n = e && e[P];
    (!n || !n.isManual_) && j(9);
    const {
      scope_: r
    } = n;
    return St(r, t), It(void 0, r);
  }
  /**
   * Pass true to automatically freeze all copies created by Immer.
   *
   * By default, auto-freezing is enabled.
   */
  setAutoFreeze(e) {
    this.autoFreeze_ = e;
  }
  /**
   * Pass true to enable strict shallow copy.
   *
   * By default, immer does not copy the object descriptors such as getter, setter and non-enumrable properties.
   */
  setUseStrictShallowCopy(e) {
    this.useStrictShallowCopy_ = e;
  }
  applyPatches(e, t) {
    let n;
    for (n = t.length - 1; n >= 0; n--) {
      const i = t[n];
      if (i.path.length === 0 && i.op === "replace") {
        e = i.value;
        break;
      }
    }
    n > -1 && (t = t.slice(n + 1));
    const r = R("Patches").applyPatches_;
    return A(e) ? r(e, t) : this.produce(e, (i) => r(i, t));
  }
};
function ct(e, t) {
  const n = Z(e) ? R("MapSet").proxyMap_(e, t) : q(e) ? R("MapSet").proxySet_(e, t) : en(e, t);
  return (t ? t.scope_ : Gt()).drafts_.push(n), n;
}
function an(e) {
  return A(e) || j(10, e), Zt(e);
}
function Zt(e) {
  if (!O(e) || Y(e)) return e;
  const t = e[P];
  let n;
  if (t) {
    if (!t.modified_) return t.base_;
    t.finalized_ = !0, n = at(e, t.scope_.immer_.useStrictShallowCopy_);
  } else
    n = at(e, !0);
  return K(n, (r, i) => {
    Bt(n, r, Zt(i));
  }), t && (t.finalized_ = !1), n;
}
var g = new rn(), on = g.produce;
g.produceWithPatches.bind(g);
g.setAutoFreeze.bind(g);
g.setUseStrictShallowCopy.bind(g);
g.applyPatches.bind(g);
g.createDraft.bind(g);
g.finishDraft.bind(g);
const Rt = {
  ar_EG: async () => {
    const [{
      default: e
    }] = await Promise.all([import("./ar_EG-DCLTp1tb.js").then((t) => t.a), import("./ar-CZx7Ft2X.js").then((t) => t.a)]);
    return {
      antd: e,
      dayjs: "ar"
    };
  },
  az_AZ: async () => {
    const [{
      default: e
    }] = await Promise.all([import("./az_AZ-BwsxY9VK.js").then((t) => t.a), import("./az-D3tAJP0S.js").then((t) => t.a)]);
    return {
      antd: e,
      dayjs: "az"
    };
  },
  bg_BG: async () => {
    const [{
      default: e
    }] = await Promise.all([import("./bg_BG-CXKtg-5i.js").then((t) => t.b), import("./bg-DeKqnkSE.js").then((t) => t.b)]);
    return {
      antd: e,
      dayjs: "bg"
    };
  },
  bn_BD: async () => {
    const [{
      default: e
    }] = await Promise.all([import("./bn_BD-DSkfmbYL.js").then((t) => t.b), import("./bn-CUmf8Qs2.js").then((t) => t.b)]);
    return {
      antd: e,
      dayjs: "bn"
    };
  },
  by_BY: async () => {
    const [{
      default: e
    }] = await Promise.all([
      import("./by_BY-l-GH0w2S.js").then((t) => t.b),
      import("./be-D-pC-f0Y.js").then((t) => t.b)
      // Belarusian (Belarus)
    ]);
    return {
      antd: e,
      dayjs: "be"
    };
  },
  ca_ES: async () => {
    const [{
      default: e
    }] = await Promise.all([import("./ca_ES-H4MmGNhj.js").then((t) => t.c), import("./ca-BDp3iz8X.js").then((t) => t.c)]);
    return {
      antd: e,
      dayjs: "ca"
    };
  },
  cs_CZ: async () => {
    const [{
      default: e
    }] = await Promise.all([import("./cs_CZ-Y4c2Vo9A.js").then((t) => t.c), import("./cs-cxAm9vfG.js").then((t) => t.c)]);
    return {
      antd: e,
      dayjs: "cs"
    };
  },
  da_DK: async () => {
    const [{
      default: e
    }] = await Promise.all([import("./da_DK-B2rJ18-4.js").then((t) => t.d), import("./da-C_EiWs8n.js").then((t) => t.d)]);
    return {
      antd: e,
      dayjs: "da"
    };
  },
  de_DE: async () => {
    const [{
      default: e
    }] = await Promise.all([import("./de_DE-D9XTXvAW.js").then((t) => t.d), import("./de-G_QpbUNG.js").then((t) => t.d)]);
    return {
      antd: e,
      dayjs: "de"
    };
  },
  el_GR: async () => {
    const [{
      default: e
    }] = await Promise.all([import("./el_GR-Far8Gusj.js").then((t) => t.e), import("./el-CN6NSsMK.js").then((t) => t.e)]);
    return {
      antd: e,
      dayjs: "el"
    };
  },
  en_GB: async () => {
    const [{
      default: e
    }] = await Promise.all([import("./en_GB-2aU2WIye.js").then((t) => t.e), import("./en-gb-DuqCHRE8.js").then((t) => t.e)]);
    return {
      antd: e,
      dayjs: "en-gb"
    };
  },
  en_US: async () => {
    const [{
      default: e
    }] = await Promise.all([import("./en_US-CgB9mWTq.js").then((t) => t.e), import("./en-a_-DF3_E.js").then((t) => t.e)]);
    return {
      antd: e,
      dayjs: "en"
    };
  },
  es_ES: async () => {
    const [{
      default: e
    }] = await Promise.all([import("./es_ES-CgGQN-mm.js").then((t) => t.e), import("./es-CRqezrhv.js").then((t) => t.e)]);
    return {
      antd: e,
      dayjs: "es"
    };
  },
  et_EE: async () => {
    const [{
      default: e
    }] = await Promise.all([import("./et_EE-CdpocEPv.js").then((t) => t.e), import("./et-Clzy7TzB.js").then((t) => t.e)]);
    return {
      antd: e,
      dayjs: "et"
    };
  },
  eu_ES: async () => {
    const [{
      default: e
    }] = await Promise.all([
      import("./eu_ES-CAzFaVr9.js").then((t) => t.e),
      import("./eu-BGiA4YQE.js").then((t) => t.e)
      // Basque
    ]);
    return {
      antd: e,
      dayjs: "eu"
    };
  },
  fa_IR: async () => {
    const [{
      default: e
    }] = await Promise.all([import("./fa_IR-BT_7nI11.js").then((t) => t.f), import("./fa-qPBwLbeY.js").then((t) => t.f)]);
    return {
      antd: e,
      dayjs: "fa"
    };
  },
  fi_FI: async () => {
    const [{
      default: e
    }] = await Promise.all([import("./fi_FI-CW6mZASH.js").then((t) => t.f), import("./fi-DZ08RUtv.js").then((t) => t.f)]);
    return {
      antd: e,
      dayjs: "fi"
    };
  },
  fr_BE: async () => {
    const [{
      default: e
    }] = await Promise.all([import("./fr_BE-BnHkOpsw.js").then((t) => t.f), import("./fr-fr_oMKVz.js").then((t) => t.f)]);
    return {
      antd: e,
      dayjs: "fr"
    };
  },
  fr_CA: async () => {
    const [{
      default: e
    }] = await Promise.all([import("./fr_CA-U-ihTOLX.js").then((t) => t.f), import("./fr-ca-jmOAx3gu.js").then((t) => t.f)]);
    return {
      antd: e,
      dayjs: "fr-ca"
    };
  },
  fr_FR: async () => {
    const [{
      default: e
    }] = await Promise.all([import("./fr_FR-HoQCBFMW.js").then((t) => t.f), import("./fr-fr_oMKVz.js").then((t) => t.f)]);
    return {
      antd: e,
      dayjs: "fr"
    };
  },
  ga_IE: async () => {
    const [{
      default: e
    }] = await Promise.all([
      import("./ga_IE-Bl9bLPc4.js").then((t) => t.g),
      import("./ga-BcI9XFsg.js").then((t) => t.g)
      // Irish
    ]);
    return {
      antd: e,
      dayjs: "ga"
    };
  },
  gl_ES: async () => {
    const [{
      default: e
    }] = await Promise.all([
      import("./gl_ES-Dfct96J8.js").then((t) => t.g),
      import("./gl-CP5p_pK_.js").then((t) => t.g)
      // Galician
    ]);
    return {
      antd: e,
      dayjs: "gl"
    };
  },
  he_IL: async () => {
    const [{
      default: e
    }] = await Promise.all([import("./he_IL-CZgo-a2w.js").then((t) => t.h), import("./he-BeDqUPrT.js").then((t) => t.h)]);
    return {
      antd: e,
      dayjs: "he"
    };
  },
  hi_IN: async () => {
    const [{
      default: e
    }] = await Promise.all([import("./hi_IN-CjX2JHn1.js").then((t) => t.h), import("./hi-DSTcoCzP.js").then((t) => t.h)]);
    return {
      antd: e,
      dayjs: "hi"
    };
  },
  hr_HR: async () => {
    const [{
      default: e
    }] = await Promise.all([import("./hr_HR-DT57_lSG.js").then((t) => t.h), import("./hr-Oe2kzLgE.js").then((t) => t.h)]);
    return {
      antd: e,
      dayjs: "hr"
    };
  },
  hu_HU: async () => {
    const [{
      default: e
    }] = await Promise.all([import("./hu_HU-DM71goO5.js").then((t) => t.h), import("./hu--QQHnNZW.js").then((t) => t.h)]);
    return {
      antd: e,
      dayjs: "hu"
    };
  },
  hy_AM: async () => {
    const [{
      default: e
    }] = await Promise.all([
      import("./hy_AM-BJ8w2SYa.js").then((t) => t.h),
      import("./am-ZpbJacDx.js").then((t) => t.a)
      // Armenian
    ]);
    return {
      antd: e,
      dayjs: "am"
    };
  },
  id_ID: async () => {
    const [{
      default: e
    }] = await Promise.all([import("./id_ID-j3xwAUXR.js").then((t) => t.i), import("./id-CHOLRxQ4.js").then((t) => t.i)]);
    return {
      antd: e,
      dayjs: "id"
    };
  },
  is_IS: async () => {
    const [{
      default: e
    }] = await Promise.all([import("./is_IS-WCcW53Gq.js").then((t) => t.i), import("./is-FOnE_KHA.js").then((t) => t.i)]);
    return {
      antd: e,
      dayjs: "is"
    };
  },
  it_IT: async () => {
    const [{
      default: e
    }] = await Promise.all([import("./it_IT-xV1BQS_S.js").then((t) => t.i), import("./it-yilKESbP.js").then((t) => t.i)]);
    return {
      antd: e,
      dayjs: "it"
    };
  },
  ja_JP: async () => {
    const [{
      default: e
    }] = await Promise.all([import("./ja_JP-bry8pUUX.js").then((t) => t.j), import("./ja--Hrn5zlT.js").then((t) => t.j)]);
    return {
      antd: e,
      dayjs: "ja"
    };
  },
  ka_GE: async () => {
    const [{
      default: e
    }] = await Promise.all([
      import("./ka_GE-__83hqcj.js").then((t) => t.k),
      import("./ka-qjFnu0L1.js").then((t) => t.k)
      // Georgian
    ]);
    return {
      antd: e,
      dayjs: "ka"
    };
  },
  kk_KZ: async () => {
    const [{
      default: e
    }] = await Promise.all([
      import("./kk_KZ-Ck1OxaWp.js").then((t) => t.k),
      import("./kk-Dnaznpne.js").then((t) => t.k)
      // Kazakh
    ]);
    return {
      antd: e,
      dayjs: "kk"
    };
  },
  km_KH: async () => {
    const [{
      default: e
    }] = await Promise.all([
      import("./km_KH-BUlPQ1y9.js").then((t) => t.k),
      import("./km-BvkXE3O1.js").then((t) => t.k)
      // Khmer
    ]);
    return {
      antd: e,
      dayjs: "km"
    };
  },
  kmr_IQ: async () => {
    const [e] = await Promise.all([
      import("./kmr_IQ-CIJqhLH6.js").then((t) => t.k)
      // Not available in Day.js, so no need to load a locale file.
    ]);
    return {
      antd: e.default,
      dayjs: ""
    };
  },
  kn_IN: async () => {
    const [{
      default: e
    }] = await Promise.all([
      import("./kn_IN-C6ML6_iB.js").then((t) => t.k),
      import("./kn-BQ0FBq5F.js").then((t) => t.k)
      // Kannada
    ]);
    return {
      antd: e,
      dayjs: "kn"
    };
  },
  ko_KR: async () => {
    const [{
      default: e
    }] = await Promise.all([import("./ko_KR-UMyyZaLw.js").then((t) => t.k), import("./ko-CA7baeYJ.js").then((t) => t.k)]);
    return {
      antd: e,
      dayjs: "ko"
    };
  },
  ku_IQ: async () => {
    const [{
      default: e
    }] = await Promise.all([
      import("./ku_IQ-DVWyHsCQ.js").then((t) => t.k),
      import("./ku-CLPkdJtx.js").then((t) => t.k)
      // Kurdish (Central)
    ]);
    return {
      antd: e,
      dayjs: "ku"
    };
  },
  lt_LT: async () => {
    const [{
      default: e
    }] = await Promise.all([import("./lt_LT-BaIWA9y4.js").then((t) => t.l), import("./lt-V-0_6SQQ.js").then((t) => t.l)]);
    return {
      antd: e,
      dayjs: "lt"
    };
  },
  lv_LV: async () => {
    const [{
      default: e
    }] = await Promise.all([import("./lv_LV-D66fEsyo.js").then((t) => t.l), import("./lv-DBMmEBwq.js").then((t) => t.l)]);
    return {
      antd: e,
      dayjs: "lv"
    };
  },
  mk_MK: async () => {
    const [{
      default: e
    }] = await Promise.all([
      import("./mk_MK-B99vnwMr.js").then((t) => t.m),
      import("./mk-B--ImrW7.js").then((t) => t.m)
      // Macedonian
    ]);
    return {
      antd: e,
      dayjs: "mk"
    };
  },
  ml_IN: async () => {
    const [{
      default: e
    }] = await Promise.all([
      import("./ml_IN-C0i42t4D.js").then((t) => t.m),
      import("./ml-DbutU47T.js").then((t) => t.m)
      // Malayalam
    ]);
    return {
      antd: e,
      dayjs: "ml"
    };
  },
  mn_MN: async () => {
    const [{
      default: e
    }] = await Promise.all([
      import("./mn_MN-UWMmp_Y7.js").then((t) => t.m),
      import("./mn-_N2ub6Xd.js").then((t) => t.m)
      // Mongolian
    ]);
    return {
      antd: e,
      dayjs: "mn"
    };
  },
  ms_MY: async () => {
    const [{
      default: e
    }] = await Promise.all([import("./ms_MY-2MioYn4A.js").then((t) => t.m), import("./ms-BU-ZVT1R.js").then((t) => t.m)]);
    return {
      antd: e,
      dayjs: "ms"
    };
  },
  my_MM: async () => {
    const [{
      default: e
    }] = await Promise.all([
      import("./my_MM-D4GyQ1EU.js").then((t) => t.m),
      import("./my-BtSysNKP.js").then((t) => t.m)
      // Burmese
    ]);
    return {
      antd: e,
      dayjs: "my"
    };
  },
  nb_NO: async () => {
    const [{
      default: e
    }] = await Promise.all([
      import("./nb_NO-T-0nGOqD.js").then((t) => t.n),
      import("./nb-C33wZx-T.js").then((t) => t.n)
      // Norwegian Bokmål
    ]);
    return {
      antd: e,
      dayjs: "nb"
    };
  },
  ne_NP: async () => {
    const [{
      default: e
    }] = await Promise.all([
      import("./ne_NP-tZihb5gO.js").then((t) => t.n),
      import("./ne-y2mNmivA.js").then((t) => t.n)
      // Nepali
    ]);
    return {
      antd: e,
      dayjs: "ne"
    };
  },
  nl_BE: async () => {
    const [{
      default: e
    }] = await Promise.all([
      import("./nl_BE-CxnY2Jb8.js").then((t) => t.n),
      import("./nl-be-Bgds5EgL.js").then((t) => t.n)
      // Dutch (Belgium)
    ]);
    return {
      antd: e,
      dayjs: "nl-be"
    };
  },
  nl_NL: async () => {
    const [{
      default: e
    }] = await Promise.all([
      import("./nl_NL-Dl_LS1KD.js").then((t) => t.n),
      import("./nl-CCSTXXaO.js").then((t) => t.n)
      // Dutch (Netherlands)
    ]);
    return {
      antd: e,
      dayjs: "nl"
    };
  },
  pl_PL: async () => {
    const [{
      default: e
    }] = await Promise.all([import("./pl_PL-qeQbjUQk.js").then((t) => t.p), import("./pl-CKdnYbRt.js").then((t) => t.p)]);
    return {
      antd: e,
      dayjs: "pl"
    };
  },
  pt_BR: async () => {
    const [{
      default: e
    }] = await Promise.all([
      import("./pt_BR-ClUUv6Ys.js").then((t) => t.p),
      import("./pt-br-DwmVYffJ.js").then((t) => t.p)
      // Portuguese (Brazil)
    ]);
    return {
      antd: e,
      dayjs: "pt-br"
    };
  },
  pt_PT: async () => {
    const [{
      default: e
    }] = await Promise.all([
      import("./pt_PT-BXzAJnFf.js").then((t) => t.p),
      import("./pt-BGr0KWGP.js").then((t) => t.p)
      // Portuguese (Portugal)
    ]);
    return {
      antd: e,
      dayjs: "pt"
    };
  },
  ro_RO: async () => {
    const [{
      default: e
    }] = await Promise.all([import("./ro_RO-BG8m0Q8L.js").then((t) => t.r), import("./ro-BZLf2WHN.js").then((t) => t.r)]);
    return {
      antd: e,
      dayjs: "ro"
    };
  },
  ru_RU: async () => {
    const [{
      default: e
    }] = await Promise.all([import("./ru_RU-Cw84WR-l.js").then((t) => t.r), import("./ru-CN1vw1lv.js").then((t) => t.r)]);
    return {
      antd: e,
      dayjs: "ru"
    };
  },
  si_LK: async () => {
    const [{
      default: e
    }] = await Promise.all([
      import("./si_LK-CMiY3wro.js").then((t) => t.s),
      import("./si-CXV5H2bF.js").then((t) => t.s)
      // Sinhala
    ]);
    return {
      antd: e,
      dayjs: "si"
    };
  },
  sk_SK: async () => {
    const [{
      default: e
    }] = await Promise.all([import("./sk_SK-8zb1ZrNu.js").then((t) => t.s), import("./sk-BpFwSOQa.js").then((t) => t.s)]);
    return {
      antd: e,
      dayjs: "sk"
    };
  },
  sl_SI: async () => {
    const [{
      default: e
    }] = await Promise.all([import("./sl_SI-CwrTvyhT.js").then((t) => t.s), import("./sl-CLA52eu-.js").then((t) => t.s)]);
    return {
      antd: e,
      dayjs: "sl"
    };
  },
  sr_RS: async () => {
    const [{
      default: e
    }] = await Promise.all([
      import("./sr_RS-DmLfdAdl.js").then((t) => t.s),
      import("./sr-MIN3XFyY.js").then((t) => t.s)
      // Serbian
    ]);
    return {
      antd: e,
      dayjs: "sr"
    };
  },
  sv_SE: async () => {
    const [{
      default: e
    }] = await Promise.all([import("./sv_SE-1Y0eG2Yb.js").then((t) => t.s), import("./sv-CqS-WO1s.js").then((t) => t.s)]);
    return {
      antd: e,
      dayjs: "sv"
    };
  },
  ta_IN: async () => {
    const [{
      default: e
    }] = await Promise.all([
      import("./ta_IN-ujvGsmnU.js").then((t) => t.t),
      import("./ta-BSUWlPw6.js").then((t) => t.t)
      // Tamil
    ]);
    return {
      antd: e,
      dayjs: "ta"
    };
  },
  th_TH: async () => {
    const [{
      default: e
    }] = await Promise.all([import("./th_TH-DUyB54at.js").then((t) => t.t), import("./th-Br5yIWbW.js").then((t) => t.t)]);
    return {
      antd: e,
      dayjs: "th"
    };
  },
  tk_TK: async () => {
    const [{
      default: e
    }] = await Promise.all([
      import("./tk_TK-C9lejDH8.js").then((t) => t.t),
      import("./tk-K_vrJcxj.js").then((t) => t.t)
      // Turkmen
    ]);
    return {
      antd: e,
      dayjs: "tk"
    };
  },
  tr_TR: async () => {
    const [{
      default: e
    }] = await Promise.all([import("./tr_TR-DUygM170.js").then((t) => t.t), import("./tr-DlAEkK4-.js").then((t) => t.t)]);
    return {
      antd: e,
      dayjs: "tr"
    };
  },
  uk_UA: async () => {
    const [{
      default: e
    }] = await Promise.all([
      import("./uk_UA-BXF8kbJy.js").then((t) => t.u),
      import("./uk-DYbUt_hF.js").then((t) => t.u)
      // Ukrainian
    ]);
    return {
      antd: e,
      dayjs: "uk"
    };
  },
  ur_PK: async () => {
    const [{
      default: e
    }] = await Promise.all([
      import("./ur_PK-DbG-WUYY.js").then((t) => t.u),
      import("./ur-qIgGqiDu.js").then((t) => t.u)
      // Urdu
    ]);
    return {
      antd: e,
      dayjs: "ur"
    };
  },
  uz_UZ: async () => {
    const [{
      default: e
    }] = await Promise.all([
      import("./uz_UZ-BAmvABqt.js").then((t) => t.u),
      import("./uz-Ctr589EZ.js").then((t) => t.u)
      // Uzbek
    ]);
    return {
      antd: e,
      dayjs: "uz"
    };
  },
  vi_VN: async () => {
    const [{
      default: e
    }] = await Promise.all([import("./vi_VN-BDsUoubr.js").then((t) => t.v), import("./vi-CkF0QKTx.js").then((t) => t.v)]);
    return {
      antd: e,
      dayjs: "vi"
    };
  },
  zh_CN: async () => {
    const [{
      default: e
    }] = await Promise.all([
      import("./zh_CN-DU6Jrst4.js").then((t) => t.z),
      import("./zh-cn-C-oIJdR9.js").then((t) => t.z)
      // Chinese (Simplified)
    ]);
    return {
      antd: e,
      dayjs: "zh-cn"
    };
  },
  zh_HK: async () => {
    const [{
      default: e
    }] = await Promise.all([
      import("./zh_HK-B2LlQ8-T.js").then((t) => t.z),
      import("./zh-hk-BFcfkcnq.js").then((t) => t.z)
      // Chinese (Hong Kong)
    ]);
    return {
      antd: e,
      dayjs: "zh-hk"
    };
  },
  zh_TW: async () => {
    const [{
      default: e
    }] = await Promise.all([
      import("./zh_TW-AvjVxBZS.js").then((t) => t.z),
      import("./zh-tw-xbLVRaz9.js").then((t) => t.z)
      // Chinese (Taiwan)
    ]);
    return {
      antd: e,
      dayjs: "zh-tw"
    };
  }
}, sn = (e, t) => on(e, (n) => {
  Object.keys(t).forEach((r) => {
    const i = r.split(".");
    let a = n;
    for (let o = 0; o < i.length - 1; o++) {
      const s = i[o];
      a[s] || (a[s] = {}), a = a[s];
    }
    a[i[i.length - 1]] = /* @__PURE__ */ I.jsx(Wt, {
      slot: t[r],
      clone: !0
    });
  });
}), un = Ke(({
  slots: e,
  themeMode: t,
  id: n,
  className: r,
  style: i,
  locale: a = "en_US",
  getTargetContainer: o,
  getPopupContainer: s,
  renderEmpty: l,
  setSlotParams: h,
  children: p,
  component: c,
  ..._
}) => {
  var u;
  const [m, k] = zt(), d = {
    dark: t === "dark",
    ...((u = _.theme) == null ? void 0 : u.algorithm) || {}
  }, y = X(s), w = X(o), E = X(l);
  Tt(() => {
    a && Rt[a] && Rt[a]().then(({
      antd: b,
      dayjs: f
    }) => {
      k(b), re.locale(f);
    });
  }, [a]);
  const v = c || ne;
  return /* @__PURE__ */ I.jsx("div", {
    id: n,
    className: r,
    style: i,
    children: /* @__PURE__ */ I.jsx(ee, {
      hashPriority: "high",
      container: document.body,
      children: /* @__PURE__ */ I.jsx(v, {
        prefixCls: "ms-gr-ant",
        ...sn(_, e),
        locale: m,
        getPopupContainer: y,
        getTargetContainer: w,
        renderEmpty: e.renderEmpty ? Ye({
          slots: e,
          setSlotParams: h,
          key: "renderEmpty"
        }) : E,
        theme: {
          cssVar: !0,
          ..._.theme,
          algorithm: Object.keys(d).map((b) => {
            switch (b) {
              case "dark":
                return d[b] ? ht.darkAlgorithm : null;
              case "compact":
                return d[b] ? ht.compactAlgorithm : null;
              default:
                return null;
            }
          }).filter(Boolean)
        },
        children: p
      })
    })
  });
});
export {
  un as ConfigProvider,
  un as default
};
